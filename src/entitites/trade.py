from datetime import datetime
from src.enums.trade_status import TradeStatus
from src.requests.trade_execution_request import TradeExecutionRequest


class Trade:
    def __init__(
        self,
        trade_id: str,
        coin: str,
        creation_time: datetime,
        trade_execution_time: datetime,
        current_price: int,
        last_evaluated_time: datetime,
        profit: int,
        target_buy_price: int,
        actual_buy_price: int,
        buy_amount_usdt: int,
        actual_sell_price: int,
        target_sell_price: int,
        stop_price: int,
        trade_resolution_time: datetime,
        trade_status: TradeStatus,
    ):
        self.trade_id = trade_id
        self.coin = coin
        self.creation_time = creation_time
        self.current_price = current_price
        self.trade_execution_time = trade_execution_time
        self.last_evaluated_time = last_evaluated_time
        self.profit = profit
        self.target_sell_price = target_sell_price
        self.target_buy_price = target_buy_price
        self.stop_price = stop_price
        self.actual_buy_price = actual_buy_price
        self.actual_sell_price = actual_sell_price
        self.buy_amount_usdt = buy_amount_usdt
        self.stop_price = stop_price
        self.trade_resolution_time = trade_resolution_time
        self.trade_status = trade_status

    def to_dict(self):
        return {
            "trade_id": self.trade_id,
            "coin": self.coin,
            "creation_time": self.creation_time,
            "trade_execution_time": self.trade_execution_time,
            "current_price": self.current_price,
            "last_evaluated_time": self.last_evaluated_time,
            "profit": self.profit,
            "target_buy_price": self.target_buy_price,
            "actual_buy_price": self.actual_buy_price,
            "actual_sell_price": self.actual_sell_price,
            "buy_amount_usdt": self.buy_amount_usdt,
            "target_sell_price": self.target_sell_price,
            "stop_price": self.stop_price,
            "trade_resolution_time": self.trade_resolution_time,
            "trade_status": self.trade_status.value,
        }

    @staticmethod
    def from_dict(data: dict):
        return Trade(
            trade_id=data["trade_id"],
            coin=data["coin"],
            trade_execution_time=(
                datetime.fromtimestamp(data["trade_execution_time"].timestamp())
                if data["trade_execution_time"] is not None
                else None
            ),
            creation_time=datetime.fromtimestamp(data["creation_time"].timestamp()),
            current_price=data["current_price"],
            actual_buy_price=data["actual_buy_price"],
            actual_sell_price=data["actual_sell_price"],
            last_evaluated_time=(
                datetime.fromtimestamp(data["last_evaluated_time"].timestamp())
                if data["last_evaluated_time"] is not None
                else None
            ),
            profit=data["profit"],
            target_sell_price=data["target_sell_price"],
            target_buy_price=data["target_buy_price"],
            buy_amount_usdt=data["buy_amount_usdt"],
            stop_price=data["stop_price"],
            trade_resolution_time=(
                datetime.fromtimestamp(data["trade_resolution_time"].timestamp())
                if data["trade_resolution_time"] is not None
                else None
            ),
            trade_status=TradeStatus(data["trade_status"]),
        )

    @staticmethod
    def from_trade_request(request: TradeExecutionRequest):
        return Trade(
            trade_id=None,
            coin=request.coin,
            creation_time=datetime.now(),
            trade_execution_time=None,
            current_price=None,
            last_evaluated_time=None,
            profit=None,
            target_sell_price=request.target_sell_price,
            actual_buy_price=None,
            actual_sell_price=None,
            target_buy_price=request.target_buy_price,
            buy_amount_usdt=request.buy_amount_usdt,
            stop_price=request.stop_price,
            trade_resolution_time=None,
            trade_status=TradeStatus.PENDING,
        )
