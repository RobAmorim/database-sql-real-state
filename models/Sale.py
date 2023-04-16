from sqlalchemy import Column, Integer, String, Float, Date, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from createConnection import Base


class Sale(Base):
    __tablename__ = 'sales'
    id = Column(Integer, primary_key=True)
    buyer_details = Column(String)
    sale_price = Column(Integer)
    date_of_sale = Column(DateTime)
    house_id = Column(Integer, ForeignKey('houses.id'))