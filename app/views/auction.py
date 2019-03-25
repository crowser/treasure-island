"""拍卖纪录"""
from flask import jsonify
from flask import request
from flask.views import MethodView
from mongoengine import Q

from app.models.auction import Auction
from app.models.auction import Status


# pylint: disable=E1101, R1719

class AuctionView(MethodView):
    """拍卖资源"""

    def get(self):

        page = request.args.get('page', default=1, type=int)
        per_page = request.args.get('per_page', default=30, type=int)

        args = {
            'productName': request.args.get('productName', type=str),
            'quality': request.args.get('quality', type=str),
            'status': request.args.get('status', default=1, type=int),
        }

        switch = {
            'productName': Q(productName__contains=args['productName']),
            'quality': Q(quality__exact=args['quality']),
            'status': Q(status__ne=Status.end.value) if is_not_end(args['status']) else Q(status=Status.end.value),
        }

        q = Q()
        for k, v in args.items():
            if v:
                q &= switch[k]

        qs = Auction.objects(q).order_by(get_order_by(args['status']))
        auctions = qs.paginate(page, per_page)

        return jsonify({
            'total': auctions.total,
            'page': {
                'pages': auctions.pages,
                'current': page,
                'per_page': per_page,
            },
            'data': [auction.to_dict() for auction in auctions.items]
        })


def is_not_end(status):
    """未结束"""
    return True if status == 1 else False


def get_order_by(status):
    """获取排序"""
    return 'endTime' if is_not_end(status) else '-endTime'
