class MCPServer:
    def __init__(self, name):
        self.name = name

    def list_tools(self):
        raise NotImplementedError

    def call_tool(self, tool_name, params):
        raise NotImplementedError