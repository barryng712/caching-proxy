import redis
from src.config.settings import Config

class Cache:
    def __init__(self):
        self.redis = redis.from_url(Config.REDIS_URL)
    
    def get(self,key):
        return self.redis.get(key)
    
    def set(self,key,value):
        self.redis.set(key,value)

    def clear(self):
        self.redis.flushdb()