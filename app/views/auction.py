"""拍卖纪录"""
from flask.views import MethodView


class Auction(MethodView):
    def get(self):
        return 'hello'
