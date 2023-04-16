from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class EstateAgent(Base):
    __tablename__ = 'estate_agent'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    office_id = Column(Integer)

