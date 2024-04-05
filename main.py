from src.services.trade_retrieval_service import TradeRetrievalService


class TradeHelperApp:

    def __init__(self):
        self.trade_retrieval_service = TradeRetrievalService()

    def get_trade_by_id(self, request):
        return self.trade_retrieval_service.get_trade_by_id(request["trade_id"])


helper_app = TradeHelperApp()


def get_trade_by_id(request):
    return helper_app.get_trade_by_id(request)
