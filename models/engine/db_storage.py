#!/usr/bin/python3
"""
Defines DBStorage class for database interaction.
"""

from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models.base_model import Base
from models import all_classes


class DBStorage:
    """
    Handles ORM operations with the database.
    """
    __engine = None
    __session = None

    def __init__(self):
        """
        Initializes the database engine and session.
        """
        user = getenv("HBNB_MYSQL_USER")
        pwd = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        db = getenv("HBNB_MYSQL_DB")
        self.__engine = create_engine(
            f"mysql+mysqldb://{user}:{pwd}@{host}/{db}", pool_pre_ping=True)
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        Queries all objects of a given class or all classes if not specified.
        """
        objs = self.__session.query(cls or all_classes).all()
        return {f"{type(obj).__name__}.{obj.id}": obj for obj in objs}

    def new(self, obj):
        """
        Adds a new object to the session.
        """
        self.__session.add(obj)

    def save(self):
        """
        Commits changes to the database.
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        Deletes an object from the session.
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """
        Creates all tables and initializes a new session.
        """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        ScopedSession = scoped_session(session_factory)
        self.__session = ScopedSession()

    def close(self):
        """
        Closes the current session.
        """
        self.__session.close()
