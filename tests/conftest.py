import pytest
import pandas as pd

from processor.transformer.transformer import Transformer


@pytest.fixture()
def meshes_test():
    data = {
        'codename': ['variant_1', 'variant_2', 'variant_3', 'variant_4', 'variant_5', 'variant_6', 'variant_1',
                     'variant_7', 'variant_9'],
        'is_compat_interior_wall': ['FALSE', 'FALSE', 'FALSE', 'FALSE', 'TRUE', 'TRUE', '0', '0', 'FAUX'],
        'mesh_width': [9.0, 3.5, 3.5, 7.4, 3.6, 6.2, 9.0, 3.0, 3.3],
        'mesh_height': [10.0, 3.8, 3.8, 7.9, 3.8, 6.0, 10.0, 3.8, 4.8],
        'mass_surf': [0.145, 0.16, 0.16, 0.225, 0.16, 0.165, 0.145, -0.22, 0.6],
        'trame': ['T2 Ra1 M4 E3', 'T2 Ra1 M2 E2', 'T3 Ra2 M2 E3', 'T3 Ra2 M2 E3', 'T2 Ra1 M2 E2', 'T3 Ra1 M3 E2',
                  'T2 Ra1 M4 E3', 'T3 Ra1 M2 E2', 'T3 Ra1 M2 E2'],
        'roll_pallet': [30.0, 33.0, 33.0, 20.0, -1.0, None, 30.0, 33.0, 33.0],
        'color_names': ['white, green, purple', 'yellow, orange, red', 'darkgrey', 'azul', 'grey', 'cyan',
                        'white, green, purple', 'yellow, orange, yellow', 'purple']
    }
    return pd.DataFrame(data)


@pytest.fixture()
def meshes_negative_test():
    data = {
        'codename': ['variant_1', 'variant_2', 'variant_3', 'variant_4', 'variant_5', 'variant_6', 'variant_1',
                     'variant_7', 'variant_9'],
        'is_compat_interior_wall': ['FALSE', 'FALSE', 'FALSE', 'FALSE', 'TRUE', 'TRUE', '0', '0', 'FAUX'],
        'mesh_width': [-9.0, 3.5, 3.5, 7.4, 3.6, 6.2, 9.0, 3.0, 3.3],
        'mesh_height': [-10.0, 3.8, 3.8, 7.9, 3.8, 6.0, 10.0, 3.8, 4.8],
        'mass_surf': [-0.145, 0.16, 0.16, 0.225, 0.16, 0.165, 0.145, -0.22, 0.6],
        'trame': ['T2 Ra1 M4 E3', 'T2 Ra1 M2 E2', 'T3 Ra2 M2 E3', 'T3 Ra2 M2 E3', 'T2 Ra1 M2 E2', 'T3 Ra1 M3 E2',
                  'T2 Ra1 M4 E3', 'T3 Ra1 M2 E2', 'T3 Ra1 M2 E2'],
        'roll_pallet': [30.0, 33.0, 33.0, 20.0, -1.0, None, 30.0, 33.0, 33.0],
        'color_names': ['white, green, purple', 'yellow, orange, red', 'darkgrey', 'azul', 'grey', 'cyan',
                        'white, green, purple', 'yellow, orange, yellow', 'purple']
    }
    return pd.DataFrame(data)


@pytest.fixture()
def transformer(meshes_test):
    return Transformer(meshes_test)
