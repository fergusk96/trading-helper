class TradeExecutionRequest:
    def __init__(
        self,
        coin: str,
        target_sell_price: int,
        stop_price: int,
        target_buy_price: int,
        buy_amount_usdt: int,
    ):
        self.coin = coin
        self.target_sell_price = target_sell_price
        self.stop_price = stop_price
        self.target_buy_price = target_buy_price
        self.buy_amount_usdt = buy_amount_usdt

    def to_dict(self):
        return {
            "coin": self.coin,
            "target_sell_price": self.target_sell_price,
            "stop_price": self.stop_price,
            "target_buy_price": self.target_buy_price,
            "buy_amount_usdt": self.buy_amount_usdt,
        }

    @staticmethod
    def from_dict(data: dict):
        return TradeExecutionRequest(
            coin=data["coin"],
            target_sell_price=data["target_sell_price"],
            stop_price=data["stop_price"],
            target_buy_price=data["target_buy_price"],
            buy_amount_usdt=data["buy_amount_usdt"],
        )
