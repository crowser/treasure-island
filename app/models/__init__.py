"""数据库初始化"""
from flask_mongoengine import MongoEngine

db = MongoEngine()


def init_db(app):
    """初始化db"""
    db.init_app(app)
