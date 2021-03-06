import os

DEBUG = os.getenv('DEBUG', '').lower() in ['1', 'true']

USE_TZ = True
TIMEZONE = 'Europe/Moscow'

# STATIC
STATIC_URL = '/static'
STATIC_PATH = 'static/'

# mongo
MONGO_URI = os.getenv('MONGO_URI', '')
MONGO_DB = os.getenv('MONGO_DB', '')

FALLBACK_ERROR_FORMAT = 'json'

REDIS_URL = os.getenv('REDIS_URL', 'redis://127.0.0.1:6379/0')

REAL_IP_HEADER = 'x-forwarded-for'
PROXIES_COUNT = 1

HOST = os.getenv('HOST')

RESPONSE_TIMEOUT = 120
