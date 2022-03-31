import redis

HOST_NAME = '127.0.0.1'
PORT = 6379

r = redis.Redis(
    host=HOST_NAME,
    port=PORT, 
    password='')


def count():
    r.set('name', 'Kristijan')
    name = r.get('name')
    return name


def reset():
    pass