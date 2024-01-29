#!/usr/bin/python3
"""This module manages storage and reload to/from a database"""

import os
from models.state import State
from models.city import City
from models.user import User
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from models.base_model import Base
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage:
    """manages storage in our db"""
    __engine = None
    __session = None
    __Session = None

    def __init__(self):
        """Initializes the SQL database storage"""
        user = os.getenv('HBNB_MYSQL_USER')
        pswd = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        db_name = os.getenv('HBNB_MYSQL_DB')
        env = os.getenv('HBNB_ENV')
        DATABASE_URL = "mysql+mysqldb://{}:{}@{}:3306/{}".format(
            user, pswd, host, db_name
        )
        self.__engine = create_engine(
            DATABASE_URL,
            pool_pre_ping=True
        )
        if env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Returns a dictionary of models present in  our storage"""
        objects = {}
        all_classes = (User, State, City, Amenity, Place, Review)
        if cls is None:
            for class_type in all_classes:
                try:
                    query = self.__session.query(class_type)
                except Exception:
                    continue
                else:
                    for obj in query.all():
                        obj_key = '{}.{}'.format(obj.__class__.__name__,
                                                 obj.id)
                        objects[obj_key] = obj
        else:
            try:
                query = self.__session.query(cls)
            except Exception as e:
                print(f"Unexpected {e=}, {type(e)=}")
            else:
                for obj in query.all():
                    obj_key = '{}.{}'.format(obj.__class__.__name__, obj.id)
                    objects[obj_key] = obj
        return objects

    def delete(self, obj=None):
        """deletes an object from the storage database"""
        if obj is not None:
            self.__session.query(type(obj)).filter(
                type(obj).id == obj.id).delete(
                synchronize_session=False)

    def new(self, obj):
        """Adds new object to storage database"""
        if obj is not None:
            try:
                self.__session.add(obj)
                self.__session.flush()
                self.__session.refresh(obj)
            except Exception as ex:
                self.__session.rollback()
                raise ex

    def save(self):
        """saves the session changes to database"""
        self.__session.commit()

    def reload(self):
        """reloads objects in the db"""
        Base.metadata.create_all(self.__engine)
        DBStorage.__Session = scoped_session(sessionmaker(
            bind=self.__engine,
            expire_on_commit=False))
        self.__session = DBStorage.__Session()

    def close(self):
        """Closes the storage engine."""
        DBStorage.__Session.remove()
