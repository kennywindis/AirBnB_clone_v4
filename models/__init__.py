#!/usr/bin/python3

"""create a unique FileStorage instance for your application"""
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from os import getenv

if getenv("HBNB_TYPE_STORAGE") == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()


"""
This file is needed to create a python package
It creates the variable storage which is used to save instances
"""
from models.engine import file_storage

storage = file_storage.FileStorage()
storage.reload()
