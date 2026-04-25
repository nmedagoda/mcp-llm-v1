import redis
import hashlib
import json
from app.config import settings

r = redis.Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, decode_responses=True)

def get_cache_key(prompt: str):
    return hashlib.md5(prompt.encode()).hexdigest()

def get_cached_response(prompt: str):
    key = get_cache_key(prompt)
    return r.get(key)

def set_cached_response(prompt: str, response: str):
    key = get_cache_key(prompt)
    r.set(key, response, ex=3600)  # TTL 1 hour