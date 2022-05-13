# TODO: create a validation mechanism:
#   * currencies should be [A-Z]{3}
#   * rate must be greater than 0
#   * valid_by_timestamp >= event_timestamp
import datetime
import decimal
from dataclasses import dataclass


@dataclass(frozen=True)
class ExchangeRate:
    """Class representing an exchange rate."""
    base_currency: str
    quote_currency: str
    rate: decimal.Decimal
    event_timestamp: datetime.datetime
    valid_by_timestamp: datetime.datetime
