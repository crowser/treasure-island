"""工具初始化"""
import sentry_sdk
from sentry_sdk.integrations.celery import CeleryIntegration
from sentry_sdk.integrations.flask import FlaskIntegration

from app.utils.exception import handle_invalid_usage
from app.utils.exception import InvalidUsage


def init_utils(app):
    """初始化工具"""
    app.register_error_handler(InvalidUsage, handle_invalid_usage)

    # 初始化sentry
    if app.config.get('SENTRY_DSN'):
        sentry_sdk.init(
            dsn=app.config.get('SENTRY_DSN'),
            integrations=[FlaskIntegration(), CeleryIntegration()]
        )
