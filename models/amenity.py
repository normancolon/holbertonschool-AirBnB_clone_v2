#!/usr/bin/python3
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class Amenity(BaseModel, Base):
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)
    amenities = relationship(
        "Place", secondary="place_amenity", back_populates="amenities")

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        from models.place import place_amenity
