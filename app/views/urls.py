"""定义url"""
from app.utils.api import Path
from .auction import Auction

paths = [
    Path(view=Auction, url="/", endpoint="index"),
]
