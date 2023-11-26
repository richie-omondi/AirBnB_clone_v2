#!/usr/bin/python
""" Module that implements class Review"""
from models.base_model import BaseModel, Base
import os
from sqlalchemy import Column, String, ForeignKey


class Review(BaseModel, Base):
    """Representation of class Review """
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'reviews'
        place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        text = Column(String(1024), nullable=False)
    else:
        place_id = ""
        user_id = ""
        text = ""

    def __init__(self, *args, **kwargs):
        """initializes Review"""
        super().__init__(*args, **kwargs)
