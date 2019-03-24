"""工具初始化"""
from app.utils.exception import handle_invalid_usage, InvalidUsage


def init_utils(app):
    """初始化工具"""
    app.register_error_handler(InvalidUsage, handle_invalid_usage)
