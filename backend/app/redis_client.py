import redis

# Configure Redis client
redis_client = redis.Redis(host='localhost', port=6379, db=0)
