from test_remote_server.main import mcp


def main():
    mcp.run(transport="http", host="0.0.0.0", port=8000)
