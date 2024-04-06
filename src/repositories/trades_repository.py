from google.cloud import firestore
from src.entitites.trade import Trade
from src.exceptions.trade_not_found_exception import TradeNotFoundException
from firesql.firebase import FirebaseClient
from firesql.sql import FireSQL
from firesql.sql.doc_printer import DocPrinter


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
        raise TradeNotFoundException(f"trade id {trade_id} not found")

    def get_trade_by_value(self, trade_id: str) -> Trade:
        trade_ref = self.firestore_client.collection("trades").where(
            "target_price", "==", 80001
        )
        trade_snapshot = trade_ref.get()
        if trade_snapshot:
            for trade in trade_snapshot:
                trade_data = trade.to_dict()
                trade_data["trade_id"] = trade.id
                return Trade.from_dict(trade_data)
        raise TradeNotFoundException(f"trade id {trade_id} not found")
