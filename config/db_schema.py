from sqlalchemy import Column, Integer, Float, String, Boolean, CheckConstraint
from sqlalchemy.types import PickleType
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Meshes(Base):
    __tablename__ = 'meshes'

    codename = Column(String(12), primary_key=True)
    trame = Column(String(50), nullable=False)
    mass_surf = Column(Float, nullable=False)
    is_compat_interior_wall = Column(Boolean, nullable=False)
    mesh_height = Column(Float, nullable=False)
    mesh_width = Column(Float, nullable=False)
    roll_pallet = Column(Integer)
    color_names = Column(PickleType, nullable=False)

    __table_args__ = (
        CheckConstraint('mass_surf > 0', name='check_positive_mass_surf'),
        CheckConstraint('mesh_height > 0', name='check_positive_mesh_height'),
        CheckConstraint('mesh_width > 0', name='check_positive_mesh_width'),
    )
