#!/usr/bin/python3
"""
   Script that defines the class State and an instance Base = declarative_base()
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

# Thsi establishs connection with the database
engine = create_engine('mysql://root:root@localhost:3306/hbtn_0e_6_usa')

# Used to map classes, and their attributes and instances to the database
Base = declarative_base()


class State(Base):
    """"
    To Inherit from the Base class and defines mapped classes
    """
    __tablename__ = "states"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
