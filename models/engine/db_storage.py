#!/usr/bin/python3
"""Database storage module for HBNB project"""
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models.base_model import Base, BaseModel
from models.state import State
from models.city import City
from models.place import Place
from models.user import User
from models.review import Review
from models.amenity import Amenity


class DBStorage:
    """Database Storage Class"""
    __engine = None
    __session = None

    def __init__(self):
        """Initialize the database storage"""
        username = getenv('HBNB_MYSQL_USER')
        password = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST', 'localhost')
        db_name = getenv('HBNB_MYSQL_DB')

        if not all([username, password, db_name]):
            raise ValueError("Missing required environment variables")

        db_url = "mysql+mysqldb://{}:{}@{}/{}".format(
            username, password, host, db_name
        )

        self.__engine = create_engine(db_url, pool_pre_ping=True)

        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)
    
    def all(self, cls=None):
        """Query on the current database session"""
        classes = {
            'State': State,
            'City': City,
            'User': User,
            'Place': Place,
            'Review': Review,
            'Amenity': Amenity
        }
        
        results = {}
        if cls:
            if isinstance(cls, str):
                cls = classes.get(cls)
            if cls:
                objs = self.__session.query(cls).all()
                for obj in objs:
                    key = f"{obj.__class__.__name__}.{obj.id}"
                    results[key] = obj
        else:
            for class_name, class_type in classes.items():
                objs = self.__session.query(class_type).all()
                for obj in objs:
                    key = f"{obj.__class__.__name__}.{obj.id}"
                    results[key] = obj
        return results

    def new(self, obj):
        """Add the object to the current database session"""
        if obj:
            self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session obj if not None"""
        if obj:
            self.__session.delete(obj)
            self.save()

    def reload(self):
        """Create all tables in the database and initialize a new session"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """Close the current session"""
        self.__session.close()