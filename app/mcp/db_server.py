from app.mcp.base import MCPServer

class DatabaseMCP(MCPServer):

    def __init__(self):
        super().__init__("database")

    def list_tools(self):
        return ["run_query"]

    def call_tool(self, tool_name, params):
        if tool_name == "run_query":
            query = params.get("query")
            return {"result": f"Executed query: {query}"}