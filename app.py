from src.services.trade_retrieval_service import TradeRetrievalService


def main():
    trade_retrieval_service = TradeRetrievalService()
    trade_retrieval_service.get_trade_by_id("9KxOnAWTUY1U0eIJuII7")


if __name__ == "__main__":
    main()
