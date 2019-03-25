"""定义url"""
from .auction import Auction
from app.utils.api import Path

# pylint: disable=E1102

paths = [
    Path(view=Auction, url="/", endpoint="index"),
]
