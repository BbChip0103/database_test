import redis

import sys

sys.path.append('../db_config')
import config

def connect_redis():
    conn = redis.Redis(host=config.REDIS_CONF['host'],
			port=config.REDIS_CONF['port'],
			password=config.REDIS_CONF['password'])
    return conn


r = connect_redis()

r.set('foo', 'bar')
value = r.get('foo')
print(value)
