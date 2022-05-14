from components.parsers.pdf_parser import PDFParser


class TestPDFParser:
    def test_get_rows(self):
        pdf_parser = PDFParser()

        assert pdf_parser.get_rows("abc", []) == [1, 2]
