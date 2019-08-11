"""
Taiga configuration file
"""
import os
from .common import *


def get_postgres_from_env():
    host = os.getenv('TAIGA_POSTGRES_HOST', 'postgres:5432').split(':')
    if len(host) == 2:
        return host[0], host[1]
    return host[0], '5432'


DEBUG = False

ALLOWED_HOSTS = ['*']

TAIGA_POSTGRES_HOST, TAIGA_POSTGRES_PORT = get_postgres_from_env()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('TAIGA_POSTGRES_NAME', 'taiga'),
        'USER': os.getenv('TAIGA_POSTGRES_USER', 'taiga'),
        'PASSWORD': os.getenv('TAIGA_POSTGRES_PASSWORD', 'DBPassword'),
        'HOST': TAIGA_POSTGRES_HOST,
        'PORT': TAIGA_POSTGRES_PORT,
    }
}

TAIGA_USER = os.getenv('TAIGA_RABBIT_USER', 'taiga')
TAIGA_PASSWORD = os.getenv('TAIGA_RABBIT_PASSWORD', 'StrongMQPassword')
TAIGA_HOST = os.getenv('TAIGA_RABBIT_HOST', 'rabbit:5672')
TAIGA_DB = os.getenv('TAIGA_RABBIT_DB', 'taiga')
TAIGA_URL = "amqp://{user}:{password}@{host}/{db}".format(
    user=TAIGA_USER,
    password=TAIGA_PASSWORD,
    host=TAIGA_HOST,
    db=TAIGA_DB
)

SECRET_KEY = 'secret_key'

MEDIA_URL = "{}/media/".format(os.getenv('TAIGA_FRONEND_URL',
                                         'http://localhost:8000'))
STATIC_URL = "{}/static/".format(os.getenv('TAIGA_FRONEND_URL',
                                           'http://localhost:8000'))
SITES["front"]["scheme"] = os.getenv('TAIGA_SCHEMA', 'http')
SITES["front"]["domain"] = os.getenv('TAIGA_DOMAIN', 'taiga')

PUBLIC_REGISTER_ENABLED = True

DEFAULT_FROM_EMAIL = os.getenv('TAIGA_EMAIL', 'mail@example.com')
SERVER_EMAIL = DEFAULT_FROM_EMAIL

EVENTS_PUSH_BACKEND = "taiga.events.backends.rabbitmq.EventsPushBackend"
EVENTS_PUSH_BACKEND_OPTIONS = {
    "url": TAIGA_URL
}
