#!/usr/bin/python3
"""
DBStorage Engine for storing and managing AirBnB objects in MySQL database
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base_model import Base
from models import storage

class DBStorage:
    """
    DBStorage class that manages database interactions for AirBnB objects
    """
    __engine = None
    __session = None

    def __init__(self):
        """
        Initialize the DB engine and session
        """
        self.__engine = create_engine(
            f"mysql+mysqldb://{storage.get('HBNB_MYSQL_USER')}:{storage.get('HBNB_MYSQL_PWD')}@{storage.get('HBNB_MYSQL_HOST')}/{storage.get('HBNB_MYSQL_DB')}", 
            pool_pre_ping=True)
        Base.metadata.create_all(self.__engine)

    def close(self):
        """
        Removes the current session from the database engine
        """
        if self.__session:
            self.__session.remove()
