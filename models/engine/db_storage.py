#!/usr/bin/python3
"""

"""
from os import getenv
from sqlalchemy import create_engine


class DBStorage:
    """
    
    """
    __engine = None
    __session = None

    def __init__(self):
        """
        
        """
        username = getenv('HBNB_MYSQL_USER')
        password = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        db_name = getenv('HBNB_MYSQL_DB')

        db_url = "mysql+mysqldb://{}:{}@{}/{}".format(username, password, host, db_name)

        self.__engine = create_engine(db_url, pool_pre_ping=True)