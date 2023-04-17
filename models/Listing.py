from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from createConnection import Base


class House(Base):
    """
    A class representing a house, with properties including an id, seller details, number of bedrooms, number of bathrooms,
    listing price, zip code, date of listing, agent id, and office id.

    Attributes:
        id (int): The unique identifier for the house.
        seller_details (str): The details of the seller.
        bedrooms (int): The number of bedrooms in the house.
        bathrooms (int): The number of bathrooms in the house.
        listing_price (float): The listing price of the house.
        zip_code (str): The zip code of the house.
        date_of_listing (datetime): The date when the house was listed.
        agent_id (int): The id of the agent associated with the house.
        office_id (int): The id of the office associated with the house.
    """
    __tablename__ = 'houses'
    id = Column(Integer, primary_key=True)
    seller_details = Column(String)
    bedrooms = Column(Integer)
    bathrooms = Column(Integer)
    listing_price = Column(Float)
    zip_code = Column(String)
    date_of_listing = Column(DateTime)
    agent_id = Column(Integer, ForeignKey('agents.id'))
    office_id = Column(Integer, ForeignKey('offices.id'))

    def __repr__(self):
        """
        Returns:
            str: A string representing the House object and house name.
        """
        return f'<House "{self.name}">'

