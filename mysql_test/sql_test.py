import sys
import pymysql

sys.path.append('../db_config')
import config

def connect_db(dbname):
    if dbname != config.MYSQL_CONF['dbname']:
        raise ValueError("Couldn't not find DB with given name")
    conn = pymysql.connect(host=config.MYSQL_CONF['host'],
                           user=config.MYSQL_CONF['user'],
                           password=config.MYSQL_CONF['password'],
                           db=config.MYSQL_CONF['dbname'])
    return conn

result = connect_db('test')
print(result)

result = connect_db('nothing')
print(result)
