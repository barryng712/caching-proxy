import os

class Config:
    REDIS_URL=os.getenv('REDIS_URL', 'redis://localhost:6379/0')
    DEFAULT_PORT=3000
    DEFAULT_ORIGIN='http://example.com'