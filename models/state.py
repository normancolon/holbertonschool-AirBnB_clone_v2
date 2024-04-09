#!/usr/bin/python3
"""
State class inherits from BaseModel and Base (respect the order)
"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import models
from models.city import City


class State(BaseModel, Base):
    """Representation of state """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state",
                          cascade="all, delete, delete-orphan")

    @property
    def cities(self):
        """Getter attribute cities that returns the list of City instances."""
        city_list = models.storage.all(City)
        return [city for city in city_list.values() if city.state_id == self.id]
