"""配置"""
import os

MONGO_USERNAME = os.environ.get('MONGO_INITDB_ROOT_USERNAME')
MONGO_PASSWORD = os.environ.get('MONGO_INITDB_ROOT_PASSWORD')
SENTRY_DSN = os.environ.get('SENTRY_DSN')

MONGODB_SETTINGS = {
    'host': f'mongodb://{MONGO_USERNAME}:{MONGO_PASSWORD}@mongo:27017/treasure_island?authSource=admin',
    'connect': False
}

# celery config
BROKER_URL = 'redis://redis:6379'
CELERY_RESULT_BACKEND = 'redis://redis:6379'
CELERY_TASK_RESULT_EXPIRES = 60 * 30
CELERYD_CONCURRENCY = 5
CELERYD_FORCE_EXECV = True
CELERYD_MAX_TASKS_PER_CHILD = 50
CELERY_DISABLE_RATE_LIMITS = True
