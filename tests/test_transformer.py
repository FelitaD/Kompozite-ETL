import pytest
import pandas as pd
from pandas.testing import assert_frame_equal

from processor.transformer.transformer import Transformer


class TestTransformer:
    def test_transform(self):
        pass

    def test_keep_unique_codename(self, transformer, meshes_test):
        actual = Transformer.keep_unique_codename(meshes_test)
        expected = meshes_test.drop(6)
        assert_frame_equal(actual, expected)
