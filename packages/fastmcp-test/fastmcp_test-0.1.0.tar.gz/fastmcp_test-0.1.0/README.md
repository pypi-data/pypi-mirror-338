# fastmcp-test

A minimal example server using `FastMCP`, providing simple tools and resources for generating random values and placeholder text. This can serve as a starting point for MCP-based APIs.

## Features

This server exposes the following:

### Tools

| Tool | Description |
|------|-------------|
| `get_random_number(min: int, max: int) -> int` | Returns a random integer between `min` and `max`. |
| `get_random_string(length: int) -> str` | Returns a random lowercase ASCII string of the specified `length`. |
| `get_random_bool() -> bool` | Returns a random boolean value (`True` or `False`). |

### Resources

| URI | Description |
|-----|-------------|
| `demo://lorem-ipsum` | Returns a static lorem ipsum string. |
| `demo://random-number` | Returns a random integer between 0 and 100. |

