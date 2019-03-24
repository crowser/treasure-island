"""处理时间"""
import time


def get_timestamp():
    """获取13位时间戳"""
    return int(time.time() * 1000)
