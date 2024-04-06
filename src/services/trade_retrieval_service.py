import json
from datetime import datetime

from flask import Response

from src.entitites.trade import Trade
from src.exceptions.trade_not_found_exception import TradeNotFoundException
from src.repositories.trades_repository import TradesRepository


class TradeRetrievalService:
    def __init__(self):
        self.trades_repository = TradesRepository()

    def get_trade_by_id(self, trade_id: str) -> Trade:
        try:
            trade = (self.trades_repository.get_trade(trade_id)).to_dict()
            json.dumps(trade, cls=DateTimeEncoder)
            return Response(
                json.dumps(trade, cls=DateTimeEncoder),
                200,
                content_type="application/json",
            )
        except TradeNotFoundException as e:
            return Response(str(e), 404, content_type="text/plain")


class DateTimeEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime):
            return o.isoformat()
        return json.JSONEncoder.default(self, o)
