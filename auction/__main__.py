"""竞拍程序"""
import threading
import time

import requests

# pylint: disable=W0621

end_time = 1553955900  # 结束时间 10位时间戳
auction_id = 114155953
price = 10
cookie = ''


def offer(auction_id, price, cookie):
    """报价"""
    url = 'https://used-api.jd.com/auctionRecord/offerPrice'
    payload = {
        'auctionId': auction_id,
        'price': price,
        'entryid': '',
        'trackId': '',
        'eid': ''
    }

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://paipai.jd.com',
        'Host': 'used-api.jd.com',
        'Accept': 'application/json, text/plain, */*',
        'Connection': 'keep-alive',
        'Accept-Language': 'zh-cn',
        'Accept-Encoding': 'br, gzip, deflate',
        'Cookie': cookie,
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.1.2 Safari/605.1.15',  # noqa: E501
        'Referer': f'https://paipai.jd.com/auction-detail/{auction_id}',
        'Content-Length': '175',
    }

    rsp = requests.post(url=url, data=payload, headers=headers)
    print(rsp.json())


def main():
    now = end_time - time.time() - 1
    timer = threading.Timer(now, offer, args=[auction_id, price, cookie])
    timer.start()


if __name__ == '__main__':
    main()
