import redis

HOST_NAME = 'redis'
PORT = 6379

r = redis.Redis(
    host=HOST_NAME,
    port=PORT, 
    password='')

#r.set('count', "0")

def count():
    r.incr('count')

def get_count():
    currentCount = str(r.get('count').decode('utf-8'))
    return currentCount


def reset():
    r.set('count', "0")

