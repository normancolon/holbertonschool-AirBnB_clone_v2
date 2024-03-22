#!/usr/bin/python3
"""
This module instantiates an object of class FileStorage or DBStorage
depending on the environment variable HBNB_TYPE_STORAGE.
"""

from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
import os
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Determine storage type based on environment variable
HBNB_TYPE_STORAGE = os.getenv('HBNB_TYPE_STORAGE', 'file')

if HBNB_TYPE_STORAGE == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    storage = FileStorage()


storage.reload()
