#!/usr/bin/python3
"""
State model for AirBnB system
"""
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy.orm import relationship

class State(BaseModel, Base):
    """
    State class represents a state in the AirBnB system
    """
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")

    def __init__(self, *args, **kwargs):
        """
        Initializes a State object
        """
        super().__init__(*args, **kwargs)

    @property
    def cities(self):
        """
        Returns the list of City objects related to the current State
        """
        from models import storage
        if storage.get("HBNB_TYPE_STORAGE") == "db":
            return self.__session.query(City).filter(City.state_id == self.id).all()
        return [city for city in storage.all(City).values() if city.state_id == self.id]
