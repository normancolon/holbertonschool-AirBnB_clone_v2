#!/usr/bin/python3
"""
This module instantiates an object of class FileStorage or DBStorage
depending on the environment variable HBNB_TYPE_STORAGE.
"""

import os
# Import the declarative base for SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

HBNB_TYPE_STORAGE = os.getenv('HBNB_TYPE_STORAGE', 'file')

if HBNB_TYPE_STORAGE == 'db':
    # DBStorage specific imports
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    # FileStorage specific imports
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

    storage.reload()
