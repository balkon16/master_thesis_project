# TODO: a PDF parser must handle encrypted PDFs
import typing
from dataclasses import dataclass
from typing import List

import PyPDF2 as p2

from components.parsers.file_parser_interface import FileParserInterface
from components.parsers.schema import Schema


@dataclass(frozen=True)
class PDFParser(FileParserInterface):
    def get_rows(self, file: typing.TextIO, schema: List[Schema]):
        # TODO: read text from a PDF file using the PyPDF2 library
        return [1, 2]