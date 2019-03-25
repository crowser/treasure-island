"""初始化celery"""
from celery import Celery
from celery.schedules import crontab

# pylint: disable=W0611

celery = Celery()

# 定义定时任务
beat_schedule = {
    'synchronization': {
        'task': "app.tasks.reptile.synchronization",
        'schedule': crontab(minute='*/30'),
    },
    "get_results": {
        "task": "app.tasks.reptile.get_results",
        "schedule": crontab(minute='*/5'),
    }
}


def init_celery(app):
    """初始化celery"""
    celery.conf.update(app.config)
    register_tasks()
    # 注册定时任务
    celery.conf.beat_schedule.update(beat_schedule)

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
    return celery


def register_tasks():
    """注册任务"""
    from . import reptile  # noqa: F401
