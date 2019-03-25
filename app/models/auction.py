"""拍卖品model"""
from enum import Enum

import mongoengine as mg

from . import db


# pylint: disable=E1101

class Status(Enum):
    notStart = 1
    progress = 2
    end = 3


class Auction(db.Document):
    auction_id = mg.IntField(unique=True)
    productName = mg.StringField(max_length=200)  # 商品名
    quality = mg.StringField(max_length=50)  # 商品成色

    startTime = mg.IntField()  # 开始拍卖时间
    endTime = mg.IntField()  # 结束拍卖时间
    status = mg.IntField()  # 商品状态
    startPrice = mg.FloatField()  # 开拍价格
    cappedPrice = mg.FloatField()  # 封顶价格
    currentPrice = mg.FloatField()  # 当前价格

    bidder = mg.StringField(max_length=50)  # 获拍者账号

    @classmethod
    def upsert(cls, data):
        return cls.objects(
            auction_id=data.get('id'),
        ).update_one(
            set__productName=data.get('productName'),
            set__quality=data.get('quality'),
            set__startTime=data.get('startTime'),
            set__endTime=data.get('endTime'),
            set__status=data.get('status'),
            set__startPrice=data.get('startPrice'),
            set__cappedPrice=data.get('cappedPrice'),
            set__currentPrice=data.get('currentPrice'),
            set__bidder=data.get('bidder'),
            upsert=True
        )
