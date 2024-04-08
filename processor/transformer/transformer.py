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
    
    def __init__(self, original_meshes):
        self.meshes = original_meshes

    def transform(self):
        """Factory function that applies all transformations."""
        self.meshes = self.meshes.convert_dtypes()
        self.meshes = self.keep_unique_codename(self.meshes)

    @staticmethod
    def keep_unique_codename(meshes):
        """Eliminate rows where codename is duplicated."""
        return meshes.drop_duplicates(subset=['codename'])

