import os

from celery import Celery
from werkzeug.utils import import_string
from app.utils.data_structure import Config

# 初始化配置
config = Config(import_string('app.conf.base'))
# load environment configuration
if 'FLASK_CONF' in os.environ:
    config = import_string(os.environ.get('FLASK_CONF'))

celery = Celery(
    __name__,
    backend=config['CELERY_RESULT_BACKEND'],
    broker=config['CELERY_BROKER_URL']
)


def init_celery(app):
    celery.conf.update(app.config)

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
    return celery


# 注册任务
from . import reptile
