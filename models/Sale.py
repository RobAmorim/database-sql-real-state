from sqlalchemy import Column, Integer, String, Float, Date
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Sale(Base):
    __tablename__ = 'sale'

    id = Column(Integer, primary_key=True)
    buyer_name = Column(String)
    sale_price = Column(Float)
    date_of_sale = Column(Date)
    estate_agent_id = Column(Integer)
    house_id = Column(Integer)

    # estate_agent = relationship("EstateAgent", back_populates="sales")
    # house = relationship("House", back_populates="sales")
