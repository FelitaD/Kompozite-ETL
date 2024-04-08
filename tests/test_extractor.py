import pytest
from pandas import DataFrame

from processor.extractor.extractor import Extractor


class TestExtractor:
    def test_extracted_type(self):
        """Tests if extracted data is of type DataFrame."""
        df = Extractor('data/dummy_meshes_with_errors.csv').extract()
        assert isinstance(df, DataFrame)
