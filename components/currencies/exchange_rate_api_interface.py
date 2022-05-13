# TODO: create a class for getting exchange rates available for private investors (as opposed to the official NBP API)

import abc
import datetime

from components.currencies.exchange_rate import ExchangeRate


class ExchangeRateAPIInterface(metaclass=abc.ABCMeta):
    methods = {
        "get_exchange_rate"
    }

    # TODO: check if a method in a subclass has the same signature
    @classmethod
    def __subclasscheck__(cls, subclass):
        if NotImplemented:
            return True

        for method in cls.methods:
            print(getattr(subclass, method))
            if not (hasattr(subclass, method) and callable(getattr(subclass, method))):
                return False

    @abc.abstractmethod
    def get_exchange_rate(self, base_currency: str, quote_currency: str, event_time: datetime.datetime,
                          time_margin: datetime.timedelta) -> ExchangeRate:
        """Load in the data set"""
        raise NotImplementedError
