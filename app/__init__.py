"""创建应用"""
import os

import flask

from .models import init_db
from .tasks import init_celery
from .utils import init_utils
from .views import init_views

app = flask.Flask(__name__)

# 初始化配置
app.config.from_object('app.conf.base')
# load environment configuration
if 'FLASK_CONF' in os.environ:
    app.config.from_envvar('FLASK_CONF')

# 初始化服务
init_db(app)
init_celery(app)

# 初始化视图
init_views(app)

# 添加工具
init_utils(app)
