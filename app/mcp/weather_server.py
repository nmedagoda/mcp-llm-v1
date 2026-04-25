from app.mcp.base import MCPServer

class WeatherMCP(MCPServer):

    def __init__(self):
        super().__init__("weather")

    def list_tools(self):
        return ["get_weather"]

    def call_tool(self, tool_name, params):
        if tool_name == "get_weather":
            city = params.get("city")
            return {"city": city, "temp": "22C", "status": "Sunny"}