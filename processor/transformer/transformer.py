import pandas as pd

from config.definitions import Fields


class Transformer:
    """Transform data into required format before loading into database."""
    
    COLS_TO_KEEP = [
        Fields.codename,
        Fields.trame,
        Fields.mass_surf,
        Fields.is_compat_interior_wall,
        Fields.mesh_height,
        Fields.mesh_width,
        Fields.roll_pallet,
        Fields.color_names
    ]

    TRAME_ALLOWED_VALUES = ["T2 Ra1 M2 E2", "T2 Ra1 M4 E2", "T2 Ra1 M4 E3"]

    COLOR_NAMES_ALLOWED_VALUES = ['white', 'yellow', 'green', 'purple', 'red', 'blue', 'orange', 'magenta', 'dark',
                                  'grey', 'cyan']

    def __init__(self, original_meshes):
        self.meshes = original_meshes

    def transform(self):
        """Factory function that applies all transformations."""
        self.meshes = self.meshes.filter(items=self.COLS_TO_KEEP)
        self.meshes = self.meshes.convert_dtypes()
        self.meshes = self.keep_unique_codename(self.meshes)
        self.meshes = self.filter_trame(self.meshes)
        self.meshes = self.filter_positive(self.meshes)
        self.meshes[Fields.is_compat_interior_wall] = self.meshes[Fields.is_compat_interior_wall].apply(self.replace_bool)
        self.meshes[Fields.roll_pallet] = self.meshes[Fields.roll_pallet].apply(self.replace_negative_roll_pallet)
        self.meshes = self.meshes[self.meshes.color_names.apply(self.check_allowed_values)]
        self.meshes = self.meshes.reset_index(drop=True)

    @staticmethod
    def keep_unique_codename(meshes):
        """Eliminate rows where codename is duplicated."""
        return meshes.drop_duplicates(subset=[Fields.codename])

    @staticmethod
    def filter_trame(meshes):
        """Filter rows where trame is not in allowed values."""
        return meshes[meshes[Fields.trame].isin(Transformer.TRAME_ALLOWED_VALUES)]

    @staticmethod
    def filter_positive(meshes):
        """Filter rows where mass_surf, mesh_height and mesh_width are positive."""
        return meshes.loc[(meshes[Fields.mass_surf] > 0) & (meshes[Fields.mesh_height] > 0) & (meshes[Fields.mesh_width] > 0)]

    @staticmethod
    def replace_bool(value):
        """Replace boolean values by Python boolean values."""
        if value in ['FAUX', 'FALSE', 'false', '0']:
            return False
        elif value in ['VRAI', 'TRUE', 'true', '1']:
            return True
        else:
            return value

    @staticmethod
    def replace_negative_roll_pallet(value):
        """Replace negative values by NA"""
        if value < 0:
            return None
        return value

    @staticmethod
    def check_allowed_values(string):
        """Check if the string contains only allowed values."""
        colors = [color.strip() for color in string.split(',')]
        for color in colors:
            if color.lower() not in Transformer.COLOR_NAMES_ALLOWED_VALUES:
                return False
        return True
    