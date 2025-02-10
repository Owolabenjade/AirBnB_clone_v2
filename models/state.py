#!/usr/bin/python3
"""
Contains the State class model
"""
import models
from os import getenv
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """
    State class for representing states in HBNB
    """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete-orphan")

    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            """
            Getter method for cities when using FileStorage
            Returns list of City objects linked to the current State
            """
            city_list = []
            for city in models.storage.all(City).values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list