from sqlalchemy import create_engine
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import sessionmaker
import pandas as pd
import struct

from config.db_schema import Meshes
from config.db_schema import Base
from config.definitions import DB_STRING, Fields


class Loader:
    """Loads pandas DataFrame into SQLite database."""
    def __init__(self):
        self.engine = create_engine(DB_STRING, echo=True)
        self.db_session = sessionmaker(bind=self.engine)

        Base.metadata.create_all(self.engine)
        Base.metadata.bind = self.engine

    def load(self, meshes):
        session = self.db_session()

        for i in range(len(meshes)):
            codename = meshes.loc[i, Fields.codename]
            trame = meshes.loc[i, Fields.trame]
            mass_surf = meshes.loc[i, Fields.mass_surf]
            is_compat_interior_wall = meshes.loc[i, Fields.is_compat_interior_wall]
            mesh_height = meshes.loc[i, Fields.mesh_height]
            mesh_width = meshes.loc[i, Fields.mesh_width]
            roll_pallet = meshes.loc[i, Fields.roll_pallet]
            color_names = meshes.loc[i, Fields.color_names]

            try:
                session.add(Meshes(
                    codename=codename,
                    trame=trame,
                    mass_surf=mass_surf,
                    is_compat_interior_wall=is_compat_interior_wall,
                    mesh_height=mesh_height,
                    mesh_width=mesh_width,
                    roll_pallet=roll_pallet,
                    color_names=color_names
                ))
                session.commit()
            except IntegrityError as e:
                print(f"Row already inserted: {e}")
                session.rollback()

    def query(self):
        session = self.db_session()

        try:
            result = session.query(Meshes).all()

            data = []
            for row in result:
                data.append([row.codename, row.trame, row.mass_surf, row.is_compat_interior_wall, row.mesh_height,
                             row.mesh_width, row.roll_pallet, row.color_names])
            print(data)

            df = pd.DataFrame(data,
                              columns=[Fields.codename,
                                       Fields.trame,
                                       Fields.mass_surf,
                                       Fields.is_compat_interior_wall,
                                       Fields.mesh_height,
                                       Fields.mesh_width,
                                       Fields.roll_pallet,
                                       Fields.color_names
                                       ])
            print(df)
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            session.close()
