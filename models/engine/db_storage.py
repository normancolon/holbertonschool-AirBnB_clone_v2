#!/usr/bin/python3
"""
Defines the DBStorage class for interfacing with the SQLAlchemy ORM.
"""

from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models.base_model import Base
from models import Amenity, City, Place, Review, State, User


class DBStorage:
    """
    Represents a database storage engine that uses SQLAlchemy for ORM operations.

    Attributes:
        __engine (sqlalchemy.Engine): The engine connected to the MySQL database.
        __session (sqlalchemy.orm.Session): The current session for database operations.
    """

    __engine = None
    __session = None

    def __init__(self):
        """Initialize the DBStorage instance with environment variables and engine configuration."""
        user = getenv("HBNB_MYSQL_USER")
        password = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        db = getenv("HBNB_MYSQL_DB")
        self.__engine = create_engine(
            f"mysql+mysqldb://{user}:{password}@{host}/{db}", pool_pre_ping=True)

        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        Query and return all objects of a given class from the current session.

        If no class is specified, returns all objects across all classes.

        Args:
            cls (type|str, optional): The class type or class name to query.

        Returns:
            dict: A dictionary of objects in the format {<class name>.<obj id>: obj}.
        """
        obj_dict = {}
        if cls:
            cls = eval(cls) if isinstance(cls, str) else cls
            objs = self.__session.query(cls).all()
        else:
            models = [State, City, User, Place, Review, Amenity]
            objs = [
                obj for model in models for obj in self.__session.query(model).all()]

        for obj in objs:
            key = f"{obj.__class__.__name__}.{obj.id}"
            obj_dict[key] = obj
        return obj_dict

    def new(self, obj):
        """Add a new object to the current session."""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current session to the database."""
        self.__session.commit()

    def delete(self, obj=None):
        """Remove an object from the current session, if it exists."""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Create all database tables and start a new session."""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        ScopedSession = scoped_session(session_factory)
        self.__session = ScopedSession()

    def close(self):
        """Close the current SQLAlchemy session."""
        self.__session.close()
