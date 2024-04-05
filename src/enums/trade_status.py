from enum import Enum


class TradeStatus(Enum):
    PENDING = 0
    OPEN = 1
    CLOSED = 2
    CANCELLED = 3
