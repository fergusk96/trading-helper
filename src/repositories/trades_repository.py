from google.cloud import firestore

from src.entitites.trade import Trade
from src.enums.trade_status import TradeStatus
from src.exceptions.trade_not_found_exception import TradeNotFoundException


class TradesRepository:

    def __init__(self):
        self.firestore_client = firestore.Client(database="trading-helper")
        self.collection = "trades"

    def get_trade(self, trade_id: str) -> Trade:
        trade_ref = self.firestore_client.collection(self.collection).document(trade_id)
        trade_snapshot = trade_ref.get()

        # Check if the document exists
        if trade_snapshot.exists:
            # Get the data from the snapshot
            trade_data = trade_snapshot.to_dict()
            trade_data["trade_id"] = trade_snapshot.id
            return Trade.from_dict(trade_data)
        raise TradeNotFoundException(f"trade id {trade_id} not found")

    def get_trade_by_value(self, trade_id: str) -> Trade:
        trade_ref = self.firestore_client.collection("trades").where(
            "stop_price", "==", 80001
        )
        trade_snapshot = trade_ref.get()
        if trade_snapshot:
            for trade in trade_snapshot:
                trade_data = trade.to_dict()
                trade_data["trade_id"] = trade.id
                return Trade.from_dict(trade_data)
        raise TradeNotFoundException(f"trade id {trade_id} not found")

    def save_trade(self, trade: Trade):
        trade_ref = self.firestore_client.collection(self.collection).document(
            trade.trade_id
        )
        trade.trade_id = trade_ref.id
        trade_ref.set(trade.to_dict())
        return trade_ref.id

    def get_trades_by_status(self, trade_status: TradeStatus) -> Trade:
        trades = []
        trades_ref = self.firestore_client.collection(self.collection).where(
            "trade_status", "==", trade_status.value
        )
        trades_snapshot = trades_ref.get()
        for trade in trades_snapshot:
            trades.append(Trade.from_dict(trade.to_dict()))
        return trades
