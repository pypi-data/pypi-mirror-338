from mcp.server.fastmcp import FastMCP

import random

mcp = FastMCP(name="fastmcp-test")


@mcp.tool()
def get_random_number(min: int, max: int) -> int:
    return random.randint(min, max)


@mcp.tool()
def get_random_string(length: int) -> str:
    return "".join(random.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(length))


@mcp.tool()
def get_random_bool() -> bool:
    return random.choice([True, False])


@mcp.resource("demo://lorem-ipsum")
def get_lorem_ipsum() -> str:
    return """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."""

@mcp.resource("demo://random-number")
def get_random_number_resource() -> int:
    return random.randint(0, 100)

def main():
    mcp.run()

if __name__ == "__main__":
    main()