from app.mcp.weather_server import WeatherMCP
from app.mcp.db_server import DatabaseMCP
from app.cache import get_cached_response, set_cached_response

weather_mcp = WeatherMCP()
db_mcp = DatabaseMCP()

def route_query(user_query: str):
    # Simple rule-based routing (replace with ML later)
    
    if "weather" in user_query.lower():
        return "weather"
    elif "sql" in user_query.lower() or "query" in user_query.lower():
        return "database"
    else:
        return "llm"

def handle_query(user_query: str):
    # 1. Cache check
    cached = get_cached_response(user_query)
    if cached:
        return {"source": "cache", "response": cached}

    # 2. Routing
    route = route_query(user_query)

    # 3. MCP or LLM
    if route == "weather":
        result = weather_mcp.call_tool("get_weather", {"city": "Auckland"})
    elif route == "database":
        result = db_mcp.call_tool("run_query", {"query": user_query})
    else:
        result = {"response": f"LLM fallback response for: {user_query}"}

    # 4. Cache store
    set_cached_response(user_query, str(result))

    return {"source": route, "response": result}