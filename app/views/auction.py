"""拍卖纪录"""
from flask.views import MethodView
from app.utils.exception import InvalidUsage


class Auction(MethodView):
    def get(self):
        raise InvalidUsage('aaa')
