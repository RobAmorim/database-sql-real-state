from sqlalchemy import Column, Integer, String, Float, Date, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from createConnection import Base


class Sale(Base):
    """
    A class representing a sale, with properties including an id, buyer details, sale price, date of sale, and house id.

    Attributes:
        id (int): The unique identifier for the sale.
        buyer_details (str): The details of the buyer.
        sale_price (int): The sale price.
        date_of_sale (datetime): The date when the sale was made.
        house_id (int): The id of the house associated with the sale.
    """
    __tablename__ = 'sales'
    id = Column(Integer, primary_key=True)
    buyer_details = Column(String)
    sale_price = Column(Integer)
    date_of_sale = Column(DateTime)
    house_id = Column(Integer, ForeignKey('houses.id'))

    def __repr__(self):
        """
        Returns:
            str: A string representing the Sale object and sale name.
        """
        return f'<Sale "{self.name}">'
