#!/usr/bin/python3
# """This module defines a class to """
# """manage storage of hbnb models in a database"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer


class Review(BaseModel, Base):
    __tablename__ = 'reviews'
    text = Column(String(1024), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    place_id = Column(String(60), ForeignKey('places.id'), nullable=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
