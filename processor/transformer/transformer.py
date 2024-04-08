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
    
    def __init__(self, original_meshes):
        self.meshes = original_meshes

    def transform(self):
        """Factory function that applies all transformations."""
        self.meshes = self.meshes.convert_dtypes()
        self.meshes = self.keep_unique_codename(self.meshes)
        self.meshes = self.filter_trame(self.meshes)

    @staticmethod
    def keep_unique_codename(meshes):
        """Eliminate rows where codename is duplicated."""
        return meshes.drop_duplicates(subset=['codename'])

    @staticmethod
    def filter_trame(meshes):
        """Filter rows where trame is not in allowed values."""
        return meshes[meshes['trame'].isin(Transformer.TRAME_ALLOWED_VALUES)]

