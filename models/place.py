#!/usr/bin/python3
"""
This module defines the Place class for the HBNB project, encapsulating
properties and behaviors of a place to stay, such as a rental property.
"""

from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from os import getenv
from models.amenity import Amenity
from models.review import Review
import models


class Place(BaseModel, Base):
    """Defines the attributes and relationships of a Place entity."""
    __tablename__ = 'places'  # Database table name

    # Place attributes:
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)

    # Relationships:
    reviews = relationship("Review", backref="place", cascade="delete")
    amenities = relationship(
        "Amenity", secondary="place_amenity", viewonly=False)

    # Association table for Place-Amenity Many-To-Many relationship
    place_amenity = Table('place_amenity', Base.metadata,
                          Column('place_id', String(60), ForeignKey(
                              'places.id'), primary_key=True, nullable=False),
                          Column('amenity_id', String(60), ForeignKey('amenities.id'), primary_key=True, nullable=False))

    amenity_ids = []  # List to hold amenity IDs (non-DB storage scenario)

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def reviews(self):
            """Retrieve list of linked Review instances."""
            return [review for review in models.storage.all(Review).values() if review.place_id == self.id]

        @property
        def amenities(self):
            """Retrieve list of linked Amenity instances."""
            return [amenity for amenity in models.storage.all(Amenity).values() if amenity.id in self.amenity_ids]

        @amenities.setter
        def amenities(self, obj):
            """Add an Amenity instance to the linked amenities list."""
            if isinstance(obj, Amenity):
                self.amenity_ids.append(obj.id)
