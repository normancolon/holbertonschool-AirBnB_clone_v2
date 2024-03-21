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
try:
    if HBNB_TYPE_STORAGE == 'db':
        from sqlalchemy.ext.declarative import declarative_base
        Base = declarative_base()
        from models.engine.db_storage import DBStorage
        storage = DBStorage()
    else:
        from models.engine.file_storage import FileStorage
        storage = FileStorage()
except ImportError as e:
    print(f"Error importing storage module: {e}")

    storage.reload()
