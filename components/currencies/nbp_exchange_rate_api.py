import datetime
import decimal
from dataclasses import dataclass
import requests

from components.currencies.exchange_rate import ExchangeRate
from components.currencies.exchange_rate_api_interface import ExchangeRateAPIInterface


@dataclass
class NBPExchangeRateAPI(ExchangeRateAPIInterface):
    """A wrapper around the official API - http://api.nbp.pl/"""
    url: str
    quote_currency: str = "PLN"

    # this is only a subset of currencies:
    currency_tables = {
        "A": {"CHF", "EUR", "USD", "GBP"},
        "B": {"KZT"}
    }

    def get_exchange_rate(self, base_currency: str, quote_currency: str, event_time: datetime.datetime,
                          time_margin: datetime.timedelta) -> ExchangeRate:
        if quote_currency != "PLN":
            raise NotImplementedError("Quote currency other than PLN is not implemented.")

        url = "http://api.nbp.pl/api/exchangerates/rates/{table}/{code}/{date}/"
        table_name = None
        for table, currencies in self.__class__.currency_tables.items():
            if base_currency in currencies:
                table_name = table

        if table_name is None:
            raise NotImplementedError(f"A base currency {base_currency} is not implemented.")

        # TODO: consider a scenario where a quote can't be find for a given day (e.g. weekend)
        resp = requests.get(url.format(table=table_name, code=base_currency, date=event_time.date()))
        if resp.status_code == 200:
            pass
        else:
            # TODO: handle an error code
            raise RuntimeError()

        # TODO: return an object of the ExchangeRate class
        return None
