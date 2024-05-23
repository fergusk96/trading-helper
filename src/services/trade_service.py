import json
from datetime import datetime

from src.entitites.trade import Trade
from src.enums.trade_status import TradeStatus
from src.repositories.trades_repository import TradesRepository
from src.services.trade_evaluation_service import TradeEvaluationService


class TradeService:
    def __init__(self):
        self.trades_repository = TradesRepository()
        self.trade_evaluation_service = TradeEvaluationService()

    def get_trade_by_id(self, trade_id: str) -> Trade:
        trade = (self.trades_repository.get_trade(trade_id)).to_dict()
        return json.dumps(trade, cls=DateTimeEncoder)

    def save_trade(self, trade: Trade):
        trade_id = self.trades_repository.save_trade(trade)
        return trade_id

    def get_open_trades(self):
        return self.trades_repository.get_trades_by_status(TradeStatus.OPEN)


class DateTimeEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime):
            return o.isoformat()
        return json.JSONEncoder.default(self, o)
