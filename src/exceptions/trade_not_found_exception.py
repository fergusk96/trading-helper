class TradeNotFoundException(Exception):
    def __init__(self, message="Trade not found"):
        self.message = message
        super().__init__(self.message)
