from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from createConnection import Base

class EstateAgent(Base):
    __tablename__ = 'estate_agents'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    phone = Column(String)
    email = Column(String)
