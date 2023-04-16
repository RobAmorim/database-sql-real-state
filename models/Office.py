from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from models.Agent import EstateAgent

Base = declarative_base()

class Office(Base):
    __tablename__ = 'office'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    location = Column(String)

    # estate_agents = relationship("EstateAgent", back_populates="office")

