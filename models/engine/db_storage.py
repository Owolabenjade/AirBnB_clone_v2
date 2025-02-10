#!/usr/bin/python3
"""
Contains the DBStorage class model
"""
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage:
    """
    DBStorage class for interfacing with MySQL database
    """
    __engine = None
    __session = None

    def __init__(self):
        """Initialize DBStorage instance"""
        user = getenv('HBNB_MYSQL_USER')
        pwd = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        db = getenv('HBNB_MYSQL_DB')
        
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            user, pwd, host, db), pool_pre_ping=True)
            
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query all objects depending on the class name"""
        classes = {
            'State': State, 'City': City, 'User': User,
            'Place': Place, 'Review': Review, 'Amenity': Amenity
        }
        results = {}
        if cls:
            if type(cls) == str:
                cls = classes[cls]
            query = self.__session.query(cls)
            for obj in query:
                key = "{}.{}".format(obj.__class__.__name__, obj.id)
                results[key] = obj
        else:
            for cls in classes.values():
                query = self.__session.query(cls)
                for obj in query:
                    key = "{}.{}".format(obj.__class__.__name__, obj.id)
                    results[key] = obj
        return results

    def new(self, obj):
        """Add object to current database session"""
        if obj:
            self.__session.add(obj)

    def save(self):
        """Commit changes to current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete object from current database session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables and session"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                     expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """
        Close the current database session and create a new one
        """
        self.__session.close()
        self.__session.remove()
        self.__session = None  # Clear the session
        self.reload()  # Create a new session