from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import select
from config.db_schema import Meshes

from config.db_schema import Base
from config.definitions import DB_STRING


class Loader:
    """Loads pandas DataFrame into SQLite database."""
    def __init__(self):
        self.engine = create_engine(DB_STRING, echo=True)
        self.db_session = sessionmaker(bind=self.engine)

        Base.metadata.create_all(self.engine)
        Base.metadata.bind = self.engine

    def load(self, meshes):
        print(type(meshes))
        meshes.to_sql('meshes', con=self.engine, if_exists='replace', index=False)

    def query(self):
        session = self.db_session()

        try:
            result = session.query(Meshes).all()

            for row in result:
                print(row)
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            session.close()
