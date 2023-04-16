from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from createConnection import Base


class Office(Base):
    __tablename__ = 'offices'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    address = Column(String)
    # estate_agent_id = Column(Integer, ForeignKey('estate_agents.id'))
