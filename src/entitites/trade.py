from datetime import datetime
from src.enums.trade_status import TradeStatus


class Trade:
    def __init__(
        self,
        trade_id: str,
        coin: str,
        creation_time: datetime,
        current_price: int,
        last_evaluated_time: datetime,
        profit: int,
        sell_price: int,
        target_price: int,
        trade_resolution_time: datetime,
        trade_status: TradeStatus,
    ):
        self.trade_id = trade_id
        self.coin = coin
        self.creation_time = creation_time
        self.current_price = current_price
        self.last_evaluated_time = last_evaluated_time
        self.profit = profit
        self.sell_price = sell_price
        self.target_price = target_price
        self.trade_resolution_time = trade_resolution_time
        self.trade_status = trade_status

    def to_dict(self):
        return {
            "trade_id": self.trade_id,
            "coin": self.coin,
            "creation_time": self.creation_time,
            "current_price": self.current_price,
            "last_evaluated_time": self.last_evaluated_time,
            "profit": self.profit,
            "sell_price": self.sell_price,
            "target_price": self.target_price,
            "trade_resolution_time": self.trade_resolution_time,
            "trade_status": self.trade_status.value,
        }

    @classmethod
    def from_dict(self, data: dict):
        self.trade_id = data["trade_id"]
        self.coin = data["coin"]
        self.creation_time = datetime.fromtimestamp(data["creation_time"].timestamp())
        self.current_price = data["current_price"]
        self.last_evaluated_time = (
            datetime.fromtimestamp(data["last_evaluated_time"].timestamp())
            if data["last_evaluated_time"] is not None
            else None
        )
        self.profit = data["profit"]
        self.sell_price = data["sell_price"]
        self.target_price = data["target_price"]
        self.trade_resolution_time = (
            datetime.fromtimestamp(data["trade_resolution_time"].timestamp())
            if data["trade_resolution_time"] is not None
            else None
        )
        self.trade_status = data["trade_status"]
        return self
