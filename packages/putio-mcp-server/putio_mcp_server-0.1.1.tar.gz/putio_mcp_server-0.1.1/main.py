import os
from typing import Any

import putiopy
from mcp.server.fastmcp import FastMCP

client = putiopy.Client(os.environ["PUTIO_TOKEN"])

mcp = FastMCP("putio")


@mcp.tool()
def list_transfers() -> list[dict[str, Any]]:
    """List active transfers."""
    transfers = client.Transfer.list()
    return [t.__dict__ for t in transfers]


@mcp.tool()
def add_transfer(url: str):
    """Add a transfer."""
    return client.Transfer.add_url(url)


@mcp.tool()
def cancel_transfer(id: int):
    """Cancel a transfer.
    If transfer is in SEEDING state, stops seeding.
    Else, removes transfer entry. Does not remove their files."""
    transfer = client.Transfer.get(id)
    return transfer.cancel()


@mcp.tool()
def get_browser_link(transfer_id: str):
    """Get a link that can be opened in a browser."""
    transfer = client.Transfer.get(transfer_id)
    file_id = transfer.file_id  # type: ignore
    if not file_id:
        return "Transfer is not completed yet. Try again later."

    return f"https://app.put.io/files/{file_id}"


def main():
    mcp.run()


if __name__ == "__main__":
    main()
