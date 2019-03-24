"""错误处理"""
from flask import jsonify


class InvalidUsage(Exception):
    """请求错误"""

    def __init__(self, error_code, status_code=400, message=''):
        super().__init__(self)

        self.error_code = error_code
        self.status_code = status_code
        self.message = message

    def to_dict(self):
        """格式化"""
        return {
            'error_code': self.error_code,
            'message': self.message
        }


def handle_invalid_usage(e: InvalidUsage):
    """错误处理器"""
    return jsonify(e.to_dict()), e.status_code
