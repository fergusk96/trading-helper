from src.services.trade_retrieval_service import TradeRetrievalService


class TradeHelperApp:

    def __init__(self):
        self.trade_retrieval_service = TradeRetrievalService()

    def get_trade_by_id(self, request):
        request_json = request.get_json()  # Parse JSON from the request body
        trade_id = request_json.get("trade_id")
        return self.trade_retrieval_service.get_trade_by_id(trade_id)


helper_app = TradeHelperApp()


def get_trade_by_id(request):
    return helper_app.get_trade_by_id(request)
