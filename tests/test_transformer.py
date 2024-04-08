import pytest
import pandas as pd
from pandas.testing import assert_frame_equal

from processor.transformer.transformer import Transformer


pd.set_option('display.max_columns', None)

class TestTransformer:
    def test_transform(self):
        pass

    def test_keep_unique_codename(self, meshes_test):
        actual = Transformer.keep_unique_codename(meshes_test)
        expected = meshes_test.drop(6)
        assert_frame_equal(actual, expected)

    def test_filter_trame(self, meshes_test):
        actual = Transformer.filter_trame(meshes_test)
        expected = meshes_test.loc[[0, 1, 4, 6]]
        assert_frame_equal(actual, expected)