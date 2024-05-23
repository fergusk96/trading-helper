import json
from datetime import datetime

from flask import Response

from src.entitites.trade import Trade
from src.enums.trade_status import TradeStatus
from src.services.trade_service import TradeService
from src.services.binance.binance_service import BinanceService


class TradeExecutionService:
    def __init__(self):
        self.trade_service = TradeService()
        self.binance_service = BinanceService()

    def execute_buy(self, trade: Trade):
        quanity = self.binance_service.calculate_amount_for_usdt(
            trade.coin, trade.buy_amount_usdt
        )
        return self.binance_service.order_asset_with_usdt(trade.coin, quanity)

    def execute_sell(self, trade: Trade, should_sell: bool):
        if not should_sell:
            return None
        return self.binance_service.sell_asset_for_ustd(
            trade.coin, trade.buy_amount_usdt
        )
