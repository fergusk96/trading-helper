from src.repositories.trades_repository import TradesRepository
from src.entitites.trade import Trade
from src.exceptions.trade_not_found_exception import TradeNotFoundException


class TradeRetrievalService:
    def __init__(self):
        self.trades_repository = TradesRepository()

    def get_trade_by_id(self, trade_id: str) -> Trade:
        try:
            return self.trades_repository.get_trade(trade_id)
        except TradeNotFoundException as e:
            response = {"statusCode": 404, "body": e.message}
            return response
