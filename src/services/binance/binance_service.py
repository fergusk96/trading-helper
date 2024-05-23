from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager
import os
import logging


class BinanceService:

    def __init__(self) -> None:
        if os.environ.get("ENV") != "PROD":
            self.client = Client(
                os.environ.get("BINANCE_API_KEY_TEST"),
                os.environ.get("BINANCE_API_SECRET_TEST"),
            )
            self.client.API_URL = "https://testnet.binance.vision/api"
        else:
            self.client = Client(
                os.environ.get("BINANCE_API_KEY"), os.environ.get("BINANCE_API_SECRET")
            )

    def get_account(self):
        return self.client.get_account()

    def get_asset_balance(self, asset):
        return self.client.get_asset_balance(asset=asset)

    def get_pair_price(self, first_asset, second_asset):
        return self.client.get_symbol_ticker(symbol=first_asset + second_asset)

    def get_all_pairs(self):
        return self.client.get_exchange_info()

    def sell_asset_for_ustd(self, asset, quantity):
        asset_balance = self.client.get_asset_balance(asset=asset)
        if float(asset_balance["free"]) < quantity:
            logging.error(
                "Insufficient balance: %s for %s, desired quantity: %s",
                asset_balance["free"],
                asset,
                quantity,
            )
            return None
        try:
            result = self.client.order_market_sell(
                symbol=asset + "USDT", quantity=quantity
            )
            logging.info("Successfully sold %s %s for USDT", quantity, asset)
            return result
        except Exception as e:
            logging.error("Error while selling %s %s for USDT: %s", quantity, asset, e)
            raise (e)

    def order_asset_with_usdt(self, asset, quantity):
        usdt_balance = self.client.get_asset_balance(asset="USDT")
        trading_price = self.get_pair_price(asset, "USDT")
        price_diff = (quantity * float(trading_price["price"])) - float(
            usdt_balance["free"]
        )
        if price_diff > 0:
            logging.error(
                "Insufficient balance of USDT: %s for asset %s, desired quantity: %s, trading price %s",
                usdt_balance["free"],
                asset,
                quantity,
                trading_price["price"],
            )
            return None
        try:
            return self.client.order_market_buy(
                symbol=asset + "USDT", quantity=quantity
            )
        except Exception as e:
            logging.error("Error while ordering %s %s for USDT: %s", quantity, asset, e)
            raise (e)

    def calculate_amount_for_usdt(self, asset, usdt_amount: float):
        trading_price = self.get_pair_price(asset, "USDT")
        return usdt_amount / float(trading_price["price"])
