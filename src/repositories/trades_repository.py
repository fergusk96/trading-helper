from google.cloud import firestore
from src.entitites.trade import Trade
from src.exceptions.trade_not_found_exception import TradeNotFoundException


class TradesRepository:

    def __init__(self):
        self.firestore_client = firestore.Client(database="trading-helper")

    def get_trade(self, trade_id: str) -> Trade:
        trade_ref = self.firestore_client.collection("trades").document(trade_id)
        trade_snapshot = trade_ref.get()

        # Check if the document exists
        if trade_snapshot.exists:
            # Get the data from the snapshot
            trade_data = trade_snapshot.to_dict()
            trade_data["trade_id"] = trade_snapshot.id
            return Trade.from_dict(trade_data)
        raise TradeNotFoundException("trade id not found")
