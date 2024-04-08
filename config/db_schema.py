from sqlalchemy import Column, Integer, Float, String, List, Boolean, ForeignKey, inspect, Table, CheckConstraint
from sqlalchemy.ext.declarative import declarative_base

from config.definitions import Fields

Base = declarative_base()


class Meshes(Base):
    __tablename__ = 'meshes'

    Fields.codename = Column(String(12), primary_key=True)
    Fields.trame = Column(String(50), nullable=False)
    Fields.mass_surf = Column(Float, nullable=False)
    Fields.is_compat_interior_wall = Column(Boolean, nullable=False)
    Fields.mesh_height = Column(Float, nullable=False)
    Fields.mesh_width = Column(Float, nullable=False)
    Fields.roll_pallet = Column(Integer)
    Fields.color_names = Column(List(String), nullable=False)

    __table_args__ = (
        CheckConstraint('mass_surf > 0', name='check_positive_mass_surf'),
        CheckConstraint('mesh_height > 0', name='check_positive_mesh_height'),
        CheckConstraint('mesh_width > 0', name='check_positive_mesh_width'),
    )
