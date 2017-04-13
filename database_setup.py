""" Database Setup File """
import sys;
from sqlalchemy import Column, ForeignKey, Integer, String, DATE, Enum, FLOAT
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

BASE = declarative_base()

### Classes ###
class Shelter(BASE):
    """ Shelter table class """
    __tablename__ = 'shelter'
    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    address = Column(String(200), nullable=False)
    city = Column(String(60), nullable=False)
    state = Column(String(60), nullable=False)
    zipCode = Column(String(5), nullable=False)
    website = Column(String(200), nullable=False)

class Puppy(BASE):
    """ Puppy table class """
    __tablename__ = 'puppy'
    id = Column(Integer, primary_key=True)
    name = Column(String(120), nullable=False)
    dateOfBirth = Column(DATE)
    gender = Column(Enum('M', 'F'), nullable=False)
    weight = Column(FLOAT)
    shelter_id = Column(Integer, ForeignKey('shelter.id'))
    picture = Column(String(200))
    shelter = relationship(Shelter)

ENGINE = create_engine('sqlite:///puppies.db')
BASE.metadata.create_all(ENGINE)
