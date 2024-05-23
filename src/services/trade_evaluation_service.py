from src.entitites.trade import Trade
from src.services.binance.binance_service import BinanceService


class TradeEvaluationService:

    def __init__(self):
        self.binance_service = BinanceService()

    def evaluate_open_trade(self, trade: Trade):
        current_price = self.binance_service.get_pair_price(trade.coin, "USDT")
        return (
            current_price >= trade.target_sell_price
            or current_price <= trade.stop_price,
            current_price,
        )

    def evaluate_potential_trade(self, trade: Trade):
        current_price = self.binance_service.get_pair_price(trade.coin, "USDT")
        return current_price <= trade.target_buy_price, current_price
