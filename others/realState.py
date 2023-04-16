# Import necessary packages
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

# Create engine
engine = create_engine('sqlite:///real_estate.db')

# Declare base
Base = declarative_base()

# Define classes
class Office(Base):
    __tablename__ = 'offices'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    agents = relationship('Agent', back_populates='office')
    
class Agent(Base):
    __tablename__ = 'agents'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    phone_number = Column(String)
    offices_id = Column(Integer, ForeignKey('offices.id'))
    office = relationship('Office', back_populates='agents')
    listings = relationship('Listing', back_populates='agent')
    sales = relationship('Sale', back_populates='agent')

class Listing(Base):
    __tablename__ = 'listings'
    id = Column(Integer, primary_key=True)
    seller_details = Column(String)
    bedrooms = Column(Integer)
    bathrooms = Column(Integer)
    listing_price = Column(Float)
    zip_code = Column(String)
    date_of_listing = Column(DateTime)
    agents_id = Column(Integer, ForeignKey('agents.id'))
    agent = relationship('Agent', back_populates='listings')
    offices_id = Column(Integer, ForeignKey('offices.id'))
    office = relationship('Office', back_populates='listings')
    sold = Column(Integer, default=0)
    sales = relationship('Sale', uselist=False, back_populates='listing')

    def calculate_commission(self, sale_price):
        if sale_price < 100000:
            commission = 0.1
        elif sale_price >= 100000 and sale_price < 200000:
            commission = 0.075
        elif sale_price >= 200000 and sale_price < 500000:
            commission = 0.06
        elif sale_price >= 500000 and sale_price < 1000000:
            commission = 0.05
        else:
            commission = 0.04
        return commission

class Sale(Base):
    __tablename__ = 'sales'
    id = Column(Integer, primary_key=True)
    buyer_details = Column(String)
    sale_price = Column(Float)
    date_of_sale = Column(DateTime)
    agents_id = Column(Integer, ForeignKey('agents.id'))
    agent = relationship('Agent', back_populates='sales')
    offices_id = Column(Integer, ForeignKey('offices.id'))
    office = relationship('Office', back_populates='sales')
    listings_id = Column(Integer, ForeignKey('listings.id'))
    listing = relationship('Listing', back_populates='sales')

    def calculate_agent_commission(self):
        commission = self.listing.calculate_commission(self.sale_price)
        return commission * self.sale_price

class Commission(Base):
    __tablename__ = 'commissions'
    id = Column(Integer, primary_key=True)
    agents_id = Column(Integer, ForeignKey('agents.id'))
    agent = relationship('Agent', back_populates='commissions')
    month = Column(String)
    year = Column(Integer)
    amount = Column(Float)

# Create tables
Base.metadata.create_all(engine)
