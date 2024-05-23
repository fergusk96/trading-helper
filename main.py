import logging
from datetime import datetime

import google.cloud.logging
from flask import Response

from src.entitites.trade import Trade
from src.enums.trade_status import TradeStatus
from src.exceptions.trade_not_found_exception import TradeNotFoundException
from src.requests.trade_execution_request import TradeExecutionRequest
from src.services.trade_evaluation_service import TradeEvaluationService
from src.services.trade_execution_service import TradeExecutionService
from src.services.trade_service import TradeService


class TradeHelperApp:

    def __init__(self):
        self.trade_service = TradeService()
        self.trade_evaluation_service = TradeEvaluationService()
        self.trade_execution_service = TradeExecutionService()

    def get_trade_by_id(self, request):
        try:
            request_json = request.get_json()  # Parse JSON from the request body
            trade_id = request_json.get("trade_id")
            return Response(
                self.trade_service.get_trade_by_id(trade_id),
                200,
                content_type="application/json",
            )
        except TradeNotFoundException as e:
            logging.error(f"Trade not found: {trade_id}")
            return Response(str(e), 404, content_type="text/plain")
        except Exception as e:
            logging.error(f"Error getting trade: {trade_id}")
            raise (e)

    def schedule_trade(self, request):
        try:
            request_json = request.get_json()  # Parse JSON from the request body
            trade_execution_request = TradeExecutionRequest.from_dict(request_json)
            trade = Trade.from_trade_request(trade_execution_request)
            return Response(
                self.trade_service.save_trade(trade), 200, content_type="text/plain"
            )
        except Exception as e:
            logging.error(f"Error saving trade: {request_json}")
            raise (e)

    def execute_workflow_start(self, event, context):
        open_trades: list[Trade] = self.trade_service.get_open_trades()
        for trade in open_trades:
            should_sell, current_price = (
                self.trade_evaluation_service.evaluate_open_trade(trade)
            )
            result = self.trade_execution_service.execute_sell(trade, should_sell)
            self._update_trade_for_sell(trade, current_price, result)
            self.trade_service.save_trade(trade)

    def _update_trade_for_buy(self, trade: Trade, current_price, result):
        now = datetime.now()
        trade.current_price = current_price
        trade.last_evaluated_time = now
        if result is None:
            return
        buy_price = self._extract_current_price_from_buy_order(result)
        trade.creation_time = now
        trade.trade_execution_time = now
        trade.profit = 0
        trade.actual_buy_price = buy_price

    def _update_trade_for_sell(self, trade: Trade, current_price, result):
        now = datetime.now()
        trade.current_price = current_price
        trade.last_evaluated_time = now
        trade.profit = current_price - trade.buy_amount_usdt

        if result is None:
            return
        current_price = self._extract_current_price_from_sell_order(result)
        trade.trade_status = TradeStatus.CLOSED
        trade.actual_sell_price = current_price
        trade.trade_resolution_time = now

    def _extract_current_price_from_buy_order(self, buy_order):
        total = 0
        for fill in buy_order["fills"]:
            total += float(fill["price"])
        return total / len(buy_order["fills"])

    def _extract_current_price_from_sell_order(self, sell_order):
        total = 0
        for fill in sell_order["fills"]:
            total += float(fill["price"])
        return total / len(sell_order["fills"])


helper_app = TradeHelperApp()
client = google.cloud.logging.Client()
client.setup_logging()


def get_trade_by_id(request):
    return helper_app.get_trade_by_id(request)


def schedule_trade(request):
    return helper_app.schedule_trade(request)


def execute_workflow_start(event, context):
    helper_app.execute_workflow_start(event, context)
