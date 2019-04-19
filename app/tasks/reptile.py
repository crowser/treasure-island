"""处理任务"""
import requests

from . import celery
from app.models.auction import Auction
from app.models.auction import Status
from app.utils.switch_time import get_timestamp


# pylint: disable=E1101

@celery.task(time_limit=60 * 10)
def synchronization():
    """同步jd待拍仓库"""
    for auction in yield_auction():
        Auction.upsert(auction)


def yield_auction():
    def send_request(page_no, page_size, get_key=None):
        try:
            response = requests.get(
                url="https://used-api.jd.com/auction/list",
                params={
                    "pageNo": page_no,
                    "pageSize": page_size,
                    "category1": "",
                    "status": "1",
                    "orderDirection": "1",
                    "orderType": "1",
                },
            )
            data = response.json().get('data')
            return data.get(get_key) if get_key else data
        except requests.exceptions.RequestException:
            print('HTTP Request failed')

    total_number = send_request(1, 1, 'totalNumber')
    page_size = 100
    total_pages = total_number // page_size + 1
    for page_no in range(total_pages, 0, -1):
        for auction in send_request(page_no, page_size, 'auctionInfos'):
            yield auction


@celery.task(time_limit=60 * 10)
def get_results():
    """获取拍卖结果"""

    def send_request(auction_id):
        try:
            response = requests.get(
                url="https://used-api.jd.com/auction/detail",
                params={
                    "auctionId": str(auction_id),
                },
            )
            return response.json().get('data').get('auctionInfo')
        except requests.exceptions.RequestException:
            print('HTTP Request failed')

    qs = Auction.objects(endTime__lt=get_timestamp(),
                         status__ne=Status.end.value).all()
    for auction in qs:
        auction = send_request(auction.auction_id)
        Auction.update(auction)
