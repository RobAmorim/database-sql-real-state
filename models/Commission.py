from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from createConnection import Base


class Commission(Base):
    __tablename__ = 'commissions'
    id = Column(Integer, primary_key=True)
    commission_amount = Column(Integer)
    sale_id = Column(Integer, ForeignKey('sales.id'))  
    estate_agent_id = Column(Integer, ForeignKey('estate_agents.id'))
