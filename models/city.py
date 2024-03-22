#!/usr/bin/python3
"""City Module for HBNB project"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)

    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))
    places = relationship("Place", backref="city")
