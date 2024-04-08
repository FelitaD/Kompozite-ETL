import pytest
import pandas as pd
from pandas.testing import assert_frame_equal

from processor.transformer.transformer import Transformer


pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)


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

    def test_filter_positive(self, meshes_negative_test):
        actual = Transformer.filter_positive(meshes_negative_test)
        expected = meshes_negative_test.loc[[1, 2, 3, 4, 5, 6, 8]]
        assert_frame_equal(actual, expected)

    def test_replace_bool(self):
        assert Transformer.replace_bool('FAUX') is False
        assert Transformer.replace_bool('VRAI') is True
        assert Transformer.replace_bool('FALSE') is False
        assert Transformer.replace_bool('TRUE') is True
        assert Transformer.replace_bool('0') is False
        assert Transformer.replace_bool('1') is True

    def test_check_allowed_values(self, meshes_test):
        actual = meshes_test[meshes_test.color_names.apply(Transformer.check_allowed_values)]
        expected = meshes_test.loc[[0, 1, 4, 5, 6, 7, 8]]
        assert_frame_equal(actual, expected)
