#!/usr/bin/python3
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv

# Assuming the place_amenity association table is defined in models.place
# and is correctly imported here if using DBStorage.


class Amenity(BaseModel, Base):
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)

    # Only establish the 'places' relationship if using DBStorage
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        # Import here to avoid circular import issues
        from models.place import place_amenity
        places = relationship(
            "Place", secondary=place_amenity, back_populates="amenities")
