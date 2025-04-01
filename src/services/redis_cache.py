import redis.asyncio as redis
from typing import Any, Optional, TypeVar
from core.config import settings


T = TypeVar('T')

class AsyncRedisCache:
    def __init__(self):
        self.redis_client = None
        
    async def init(self):
        """Initialize Redis connection pool"""
        if self.redis_client is None:
            self.redis_client = await redis.from_url(settings.REDIS_URL, encoding="utf-8", decode_responses=True)
        
    async def close(self):
        """Close Redis connection pool"""
        if self.redis_client:
            await self.redis_client.close()
            self.redis_client = None
            
    async def get(self, key: str) -> Optional[str]:
        """Get value from cache by key"""
        await self.init()
        return await self.redis_client.get(key)
    
    async def set(self, key: str, value: Any, ttl: int = None) -> bool:
        """Set value in cache with optional TTL (in seconds)"""
        await self.init()
        if ttl is None:
            ttl = settings.CACHE_TTL
        return await self.redis_client.set(key, value, ex=ttl)
    
    async def delete(self, key: str) -> int:
        """Delete a key from cache"""
        await self.init()
        return await self.redis_client.delete(key)
    
    def generate_key(self, base: str, *args) -> str:
        """Generate a cache key from base and arguments"""
        return f"{base}:{':'.join(str(arg) for arg in args)}"

# Create a singleton instance
cache = AsyncRedisCache()