#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import sys
# No need for asyncio import if handlers are sync

# Configure basic logging BEFORE creating FastMCP instance
# Crucially, log to stderr for stdio transport
logging.basicConfig(
    level=logging.INFO,  # Set to DEBUG for more verbose MCP communication logs
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    stream=sys.stderr,  # Log to stderr!
)

# Assuming mcp library is correctly installed
from mcp.server.fastmcp import FastMCP
from mcp import types

# --- Server Definition ---

mcp = FastMCP(title="ExamplePromptServer")

# --- Prompt Definitions ---

# Define the prompts this server offers (same as before)
AVAILABLE_PROMPTS = [
    types.Prompt(
        name="say-hello-to-mom",
        description="Sends message to mom",
        arguments=[
            types.PromptArgument(
                name="message",
                description="the message to be sent",
                type="string",
                required=True,
            )
        ],
    )
]

for prompt in AVAILABLE_PROMPTS:
    mcp.add_prompt(prompt)


@mcp.tool()
async def say_hello_to_mom(message: str):
    """Send message to mom

    Args:
        message: the message to be sent
    """
    return "Message sent successfully"


if __name__ == "__main__":
    mcp.run()
