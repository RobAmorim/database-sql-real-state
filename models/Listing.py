from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from createConnection import Base


class House(Base):
    __tablename__ = 'houses'
    id = Column(Integer, primary_key=True)
    seller_details = Column(String)
    bedrooms = Column(Integer)
    bathrooms = Column(Integer)
    listing_price = Column(Float)
    zip_code = Column(String)
    date_of_listing = Column(DateTime)
    estate_agent_id = Column(Integer, ForeignKey('estate_agents.id'))
    office_id = Column(Integer, ForeignKey('offices.id'))
