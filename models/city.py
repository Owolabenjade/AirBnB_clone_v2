#!/usr/bin/python3
""" holds class City"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """Representation of city"""
    if models.storage_t == "db":
        __tablename__ = 'cities'
        state_id = Column(String(60), ForeignKey('states.id', ondelete='CASCADE'),
                         nullable=False)
        name = Column(String(128), nullable=False)
        places = relationship("Place", backref="cities",
                            cascade="all, delete-orphan",
                            passive_deletes=True)
    else:
        state_id = ""
        name = ""

    def __init__(self, *args, **kwargs):
        """initializes city"""
        super().__init__(*args, **kwargs)

    def __str__(self):
        """String representation of the City instance"""
        return "[City] ({}) {}".format(self.id, self.__dict__)

    @property
    def state(self):
        """getter for associated state"""
        if models.storage_t == "db":
            from models.state import State
            return models.storage.get(State, self.state_id)
        return None