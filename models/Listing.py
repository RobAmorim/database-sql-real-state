from sqlalchemy import Column, Integer, String, Float, Date
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class House(Base):
    __tablename__ = 'house'

    id = Column(Integer, primary_key=True)
    seller_name = Column(String)
    num_bedrooms = Column(Integer)
    num_bathrooms = Column(Integer)
    listing_price = Column(Float)
    zip_code = Column(String)
    date_of_listing = Column(Date)
    estate_agent_id = Column(Integer)

    # sales = relationship("Sale", back_populates="house")
