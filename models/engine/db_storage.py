#!/usr/bin/python3
"""
Defines the DBStorage class for database interactions.
"""

from sqlalchemy import create_engine
from os import getenv
import sys
from models.base_model import Base
from sqlalchemy.orm import sessionmaker, scoped_session
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        """Initializes the DBStorage class with database connection."""
        user = getenv("HBNB_MYSQL_USER")
        passwd = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        database = getenv("HBNB_MYSQL_DB")
        env = getenv("HBNB_ENV")

        self.__engine = create_engine(
            f"mysql+mysqldb://{user}:{passwd}@{host}/{database}",
            pool_pre_ping=True)
        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):

        obj_dict = {}
        if cls:
            if isinstance(cls, str):
                cls = getattr(sys.modules[__name__], cls)
            query = self.__session.query(cls)
            for obj in query:
                key = f"{type(obj).__name__}.{obj.id}"
                obj_dict[key] = obj
        else:
            classes = [User, State, City, Place, Review, Amenity]
            for cls in classes:
                query = self.__session.query(cls)
                for obj in query:
                    key = f"{type(obj).__name__}.{obj.id}"
                    obj_dict[key] = obj
        return obj_dict

    def new(self, obj):
        """Adds an object to the current database session."""
        self.__session.add(obj)

    def save(self):
        """Commits all changes in the current database session."""
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes an object from the current database session if provided."""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Creates all tables in the database and initializes a new session."""
        Base.metadata.create_all(self.__engine)
        Session = scoped_session(sessionmaker(
            bind=self.__engine, expire_on_commit=False))
        self.__session = Session()

    def close(self):
        """Closes the current session."""
        self.__session.close()
