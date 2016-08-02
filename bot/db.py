import redis
import os 
import pickle

redis_url =  os.environ.get('REDIS_URL', 'redis://localhost:6379/0')
print(redis_url)
redis_store = redis.StrictRedis.from_url(redis_url)

def redis_get(id):
    return pickle.loads(redis_store[id])

def redis_set(id, data):
    json_data = pickle.dumps(data)
    redis_store[id] = json_data

def redis_del(id):
    del redis_store[id]