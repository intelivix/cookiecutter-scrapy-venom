# -*- coding: utf-8 -*-

from decouple import config
from scrapy_venom.management.registers import register_spiders
from scrapy_venom.management.registers import register_pipelines

PROJECT_NAME = '{{cookiecutter.project_name}}'

BOT_NAME = PROJECT_NAME

MANAGE_COMMANDS_PATH = '{}.commands'.format(PROJECT_NAME)

USER_AGENT = config('USER_AGENT', default='Spider')


SPIDER_MODULES = register_spiders(
    'sample'
)

ITEM_PIPELINES = register_pipelines({
    'sample.SamplePipeline': 800,
})


# AUTOTHROTTLE

AUTOTHROTTLE_ENABLED = config(
    'AUTOTHROTTLE_ENABLED', default=True, cast=bool)

AUTOTHROTTLE_START_DELAY = config(
    'AUTOTHROTTLE_START_DELAY', default=5.0, cast=float)

AUTOTHROTTLE_MAX_DELAY = config(
    'AUTOTHROTTLE_MAX_DELAY', default=15.0, cast=float)

AUTOTHROTTLE_DEBUG = config(
    'AUTOTHROTTLE_DEBUG', default=False, cast=bool)


# CONCURRENCY

CONCURRENT_REQUESTS = config(
    'CONCURRENT_REQUESTS', default=16, cast=int)

CONCURRENT_REQUESTS_PER_IP = config(
    'CONCURRENT_REQUESTS_PER_IP', default=2, cast=int)


# DATABASE

# MONGODB
USE_MONGO = config('USE_MONGODB', False)
if USE_MONGO:
    MONGODB_SERVER = config('MONGODB_SERVER', default='localhost')
    MONGODB_PORT = config('MONGODB_PORT', default=27017)
    MONGODB_DB = config('MONGODB_DB')

# POSTGRESQL
USE_POSTGRESQL = config('USE_POSTGRESQL', False)
if USE_POSTGRESQL:
    POSTGRESQL_DATABASE = {
        'drivername': config('DB_DRIVER', default='postgres'),
        'host': config('DB_HOST', default='localhost'),
        'port': config('DB_PORT', default='5432'),
        'username': config('DB_USER'),
        'password': config('DB_PASS'),
        'database': config('DB_NAME'),
    }

# LOG

LOG_ENABLED = config(
    'LOG_ENABLED', default=False, cast=bool)

LOG_FILE = config(
    'LOG_FILE', default='scrapy-tribunais.log')


# SENTRY

if config('USE_SENTRY', default=False, cast=bool):
    SENTRY_DSN = config('SENTRY_DSN')
    EXTENSIONS = {
        'scrapy_sentry.extensions.Errors': 10,
    }
