#!/usr/bin/python3
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

# Assuming the place_amenity association table is defined in models.place
# and is correctly imported here if using DBStorage.


class Amenity(BaseModel, Base):
    """Amenity class representing an amenity of a place."""
    __tablename__ = 'amenities'

    name = Column(String(128), nullable=False)

    place_amenities = relationship("Place", secondary="place_amenity")
