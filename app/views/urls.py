"""定义url"""
from .auction import AuctionView
from app.utils.api import Path

# pylint: disable=E1102

paths = [
    Path(view=AuctionView, url="/auctions", endpoint="auction"),
]
