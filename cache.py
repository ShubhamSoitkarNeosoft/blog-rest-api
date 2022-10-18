from flask_caching import Cache

# cache = Cache()
cache = Cache(config={
    'CACHE_TYPE':'redis',
    'CACHE_KEY_PREFIX':'server1',
    'CACHE_REDIS_HOST':'localhost',
    'CACHE_REDIS_PORT':'6379',
    'CACHE_DEFAULT_TIMEOUT': 300,
    'CACHE_REDIS_URL':'redis://localhost:6379/0'
    })