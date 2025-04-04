#!/usr/bin/env python3
import asyncio
import base64
import logging
import os
import random
import sys
from contextlib import closing
from typing import Any, Dict, List, Optional

from mcp.server.models import InitializationOptions
from mcp.server import NotificationOptions, Server
import mcp.server.stdio
import mcp.types as types
from pydantic import AnyUrl

from .db import (
    create_round,
    get_last_round,
    get_round,
    submit_guess,
    reveal_twist,
    get_total_rounds,
    get_score,
    get_twist_index_stats,
    upgrade_db,
)

# reconfigure UnicodeEncodeError prone default (i.e. windows-1252) to utf-8
if sys.platform == "win32" and os.environ.get('PYTHONIOENCODING') is None:
    sys.stdin.reconfigure(encoding="utf-8")
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

logger = logging.getLogger('ttaat_mcp_server')
logger.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stderr)
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

class TtaatGameServer:
    def __init__(self):
        """Initialize the TTAAT game server."""
        # First, make sure the database is initialized
        was_upgraded, _, _ = upgrade_db()
        if was_upgraded:
            logger.info("Database was upgraded to the latest version")
        else:
            logger.info("Database is already at the latest version")
        
        self.server = Server("ttaat-game")
        
        # Register handlers using decorators
        @self.server.list_tools()
        async def handle_list_tools_request():
            return await self.handle_list_tools()
            
        @self.server.call_tool()
        async def handle_call_tool_request(name: str, arguments: Dict[str, Any] | None):
            return await self.handle_call_tool(name, arguments)

    async def handle_list_tools(self) -> List[types.Tool]:
        """List available tools for the TTAAT game."""
        logger.debug("Handling list_tools request")
        return [
            types.Tool(
                name="create_round",
                description=f"Create a new game round with a question and three statements. IMPORTANT: There must be EXACTLY 2 true statements and 1 twist statement - no more, no less. The twist should be playful, surprising, and entertaining - not just factually incorrect. Make sure the TRUE statements are grounded in actual facts - use web searches or your knowledge base as needed to verify information. If you have image or audio generation capabilities, use them to create relevant, engaging visuals or sounds to accompany your question and statements. Note the current twist position distribution is {get_twist_index_stats()} - try to vary your twist position while keeping it unpredictable (don't be too obvious about balancing the distribution).",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "category": {"type": "string", "description": "The category of the question"},
                        "question": {"type": "string", "description": "The main question for the round"},
                        "trivia_1": {"type": "string", "description": "First statement - can be truth or twist"},
                        "trivia_2": {"type": "string", "description": "Second statement - can be truth or twist"},
                        "trivia_3": {"type": "string", "description": "Third statement - can be truth or twist"},
                    },
                    "required": ["category", "question", "trivia_1", "trivia_2", "trivia_3"],
                },
            ),
            types.Tool(
                name="submit_guess",
                description="Submit a player's guess for which statement is the twist",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "round_id": {"type": "integer", "description": "The ID of the round"},
                        "guess_index": {"type": "integer", "description": "Index of the guessed statement (0, 1, or 2)"},
                    },
                    "required": ["round_id", "guess_index"],
                },
            ),
            types.Tool(
                name="reveal_twist",
                description="Reveal which statement was the twist and provide explanations. The explanations should be entertaining and playful - build anticipation and make the reveal fun! If you have image or audio generation capabilities, use them to enhance the reveal and make it more engaging and memorable.",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "round_id": {"type": "integer", "description": "The ID of the round"},
                        "twist_index": {"type": "integer", "description": "Index of the twist statement (0, 1, or 2)"},
                        "explanation_1": {"type": "string", "description": "Explanation for statement 1 - be creative and entertaining"},
                        "explanation_2": {"type": "string", "description": "Explanation for statement 2 - be creative and entertaining"},
                        "explanation_3": {"type": "string", "description": "Explanation for statement 3 - be creative and entertaining"},
                    },
                    "required": ["round_id", "twist_index", "explanation_1", "explanation_2", "explanation_3"],
                },
            ),
            types.Tool(
                name="get_round",
                description="Get details of a specific round",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "round_id": {"type": "integer", "description": "The ID of the round to retrieve"},
                    },
                    "required": ["round_id"],
                },
            ),
            types.Tool(
                name="get_last_round",
                description="Get details of the most recent round",
                inputSchema={
                    "type": "object",
                    "properties": {},
                },
            ),
            types.Tool(
                name="get_stats",
                description="Get game statistics",
                inputSchema={
                    "type": "object",
                    "properties": {},
                },
            ),
            types.Tool(
                name="get_entropy",
                description="Get a base64 encoded random 64-bit integer for use as entropy. You can call this before create_round and use the resulting random number to fairly determine which statement should be the twist (0, 1, or 2). This helps create an unbiased distribution of twist positions and makes the game more challenging for players.",
                inputSchema={
                    "type": "object",
                    "properties": {},
                },
            ),
        ]

    async def handle_call_tool(
        self, name: str, arguments: Dict[str, Any] | None
    ) -> List[types.TextContent | types.ImageContent | types.EmbeddedResource]:
        """Handle tool execution requests."""
        logger.debug(f"Handling call_tool request for {name} with args {arguments}")
        try:
            # Dispatch to the appropriate handler method based on the tool name
            handler_map = {
                "create_round": self._handle_create_round,
                "submit_guess": self._handle_submit_guess,
                "reveal_twist": self._handle_reveal_twist,
                "get_round": self._handle_get_round,
                "get_last_round": self._handle_get_last_round,
                "get_stats": self._handle_get_stats,
                "get_entropy": self._handle_get_entropy,
            }
            
            if name in handler_map:
                return await handler_map[name](arguments)
            else:
                raise ValueError(f"Unknown tool: {name}")
                
        except Exception as e:
            logger.error(f"Error handling tool call: {e}")
            return [types.TextContent(
                type="text", 
                text=f"Error: {str(e)}",
                isError=True
            )]
    
    async def _handle_create_round(self, arguments: Dict[str, Any] | None) -> List[types.TextContent]:
        if not arguments:
            raise ValueError("Missing arguments")
        
        required_args = ["category", "question", "trivia_1", "trivia_2", "trivia_3"]
        for arg in required_args:
            if arg not in arguments:
                raise ValueError(f"Missing required argument: {arg}")
        
        round_id = create_round(
            arguments["category"],
            arguments["question"],
            arguments["trivia_1"],
            arguments["trivia_2"],
            arguments["trivia_3"]
        )
        
        return [types.TextContent(
            type="text", 
            text=f"Round created successfully with ID: {round_id}"
        )]
    
    async def _handle_submit_guess(self, arguments: Dict[str, Any] | None) -> List[types.TextContent]:
        if not arguments or "round_id" not in arguments or "guess_index" not in arguments:
            raise ValueError("Missing required arguments: round_id and guess_index")
        
        round_id = arguments["round_id"]
        guess_index = arguments["guess_index"]
        
        if not isinstance(guess_index, int) or guess_index not in [0, 1, 2]:
            raise ValueError("guess_index must be 0, 1, or 2")
        
        submit_guess(round_id, guess_index)
        
        return [types.TextContent(
            type="text", 
            text=f"Guess submitted for round {round_id}: statement #{guess_index + 1}"
        )]
    
    async def _handle_reveal_twist(self, arguments: Dict[str, Any] | None) -> List[types.TextContent]:
        if not arguments:
            raise ValueError("Missing arguments")
        
        required_args = ["round_id", "twist_index", "explanation_1", "explanation_2", "explanation_3"]
        for arg in required_args:
            if arg not in arguments:
                raise ValueError(f"Missing required argument: {arg}")
        
        round_id = arguments["round_id"]
        twist_index = arguments["twist_index"]
        
        if not isinstance(twist_index, int) or twist_index not in [0, 1, 2]:
            raise ValueError("twist_index must be 0, 1, or 2")
        
        reveal_twist(
            round_id,
            twist_index,
            arguments["explanation_1"],
            arguments["explanation_2"],
            arguments["explanation_3"]
        )
        
        return [types.TextContent(
            type="text", 
            text=f"Twist revealed for round {round_id}: statement #{twist_index + 1}"
        )]
    
    async def _handle_get_round(self, arguments: Dict[str, Any] | None) -> List[types.TextContent]:
        if not arguments or "round_id" not in arguments:
            raise ValueError("Missing required argument: round_id")
        
        round_id = arguments["round_id"]
        round_data = get_round(round_id)
        
        if not round_data:
            return [types.TextContent(
                type="text", 
                text=f"No round found with ID: {round_id}"
            )]
        
        return [types.TextContent(
            type="text", 
            text=str(round_data)
        )]
    
    async def _handle_get_last_round(self, arguments: Dict[str, Any] | None) -> List[types.TextContent]:
        round_data = get_last_round()
        
        if not round_data:
            return [types.TextContent(
                type="text", 
                text="No rounds found"
            )]
        
        return [types.TextContent(
            type="text", 
            text=str(round_data)
        )]
    
    async def _handle_get_stats(self, arguments: Dict[str, Any] | None) -> List[types.TextContent]:
        total_rounds = get_total_rounds()
        player_score, gm_score = get_score()
        twist_stats = get_twist_index_stats()
        
        stats = {
            "total_rounds": total_rounds,
            "player_score": player_score,
            "gm_score": gm_score,
            "twist_distribution": twist_stats
        }
        
        return [types.TextContent(
            type="text", 
            text=str(stats)
        )]
        
    async def _handle_get_entropy(self, arguments: Dict[str, Any] | None) -> List[types.TextContent]:
        """Generate and return a base64 encoded random 64-bit integer."""
        # Generate a random 64-bit integer (8 bytes)
        random_int = random.getrandbits(64)
        
        # Convert to bytes (8 bytes for a 64-bit integer)
        random_bytes = random_int.to_bytes(8, byteorder='big')
        
        # Encode as base64
        base64_encoded = base64.b64encode(random_bytes).decode('utf-8')
        
        return [types.TextContent(
            type="text", 
            text=base64_encoded
        )]

    async def start_server(self):
        """Start the MCP server for TTAAT."""
        logger.info("Starting Two Truths and a Twist MCP Server")
        
        async with mcp.server.stdio.stdio_server() as (read_stream, write_stream):
            logger.info("Server running with stdio transport")
            await self.server.run(
                read_stream,
                write_stream,
                InitializationOptions(
                    server_name="ttaat",
                    server_version="0.1.6",
                    capabilities=self.server.get_capabilities(
                        notification_options=NotificationOptions(),
                        experimental_capabilities={},
                    ),
                ),
            )


def serve_mcp():
    """Start the TTAAT MCP server."""
    # Initialize and start the server
    game_server = TtaatGameServer()
    asyncio.run(game_server.start_server())


if __name__ == "__main__":
    serve_mcp()