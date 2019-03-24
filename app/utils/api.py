"""api工具"""
import typing
from flask.views import MethodView
from flask.blueprints import Blueprint

_METHODS = ('GET', 'POST', 'PUT', 'PATCH', 'DELETE')

Path = typing.NamedTuple("Path", view=MethodView, url=str, endpoint=str)


def batch_register_api(blueprint: Blueprint, paths: typing.List[Path]) -> None:
    """批量注册 api"""
    for path in paths:
        view_func = path.view.as_view(path.endpoint)
        blueprint.add_url_rule(path.url, path.endpoint, view_func, methods=_METHODS)
