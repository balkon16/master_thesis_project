import abc
import typing
from typing import List

from components.parsers.schema import Schema


class FileParserInterface(metaclass=abc.ABCMeta):
    methods = {
        "get_rows"
    }

    # TODO (low): check if a method in a subclass has the same signature
    @classmethod
    def __subclasscheck__(cls, subclass):
        if NotImplemented:
            return True

        for method in cls.methods:
            print(getattr(subclass, method))
            if not (hasattr(subclass, method) and callable(getattr(subclass, method))):
                return False

    def get_rows(self, file: typing.TextIO, schema: List[Schema]):  # TODO: should return an list of Row(s)
        """Parse contents of a file or a file-like object to rows with a given schema."""
        raise NotImplementedError
