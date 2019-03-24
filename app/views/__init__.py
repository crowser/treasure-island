"""视图初始化"""
from flask import Blueprint
from .urls import paths
from app.utils.api import batch_register_api

depot = Blueprint("auction", __name__)

batch_register_api(depot, paths)


def init_views(app):
    """初始化视图"""
    app.register_blueprint(depot)
