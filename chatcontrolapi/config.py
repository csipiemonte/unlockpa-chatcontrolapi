from configparser import ConfigParser, RawConfigParser
from os import environ  

config = ConfigParser()
config.read('config.ini')


# Import edited settings from ENV
config.set('DB', 'DBHOST', environ['POSTGRES_URL'])
config.set('DB', 'DBPORT', environ['POSTGRES_PORT'])
config.set('DB', 'PASSWORD', environ['POSTGRES_PASSWORD'])
config.set('DB', 'USER', environ['POSTGRES_USER'])
config.set('DB', 'DATABASE', environ['POSTGRES_DB'])
config.set('DB', 'SCHEMA', environ['POSTGRES_SCHEMA'])


configSql = RawConfigParser()
configSql.read('configSql.ini')
