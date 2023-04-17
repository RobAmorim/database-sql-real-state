from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import date
from models.Sale import Sale
from models.Agent import Agent
from models.Listing import House
from faker import Faker

def populate(session, num):
    """
    Populates the sale table with fake data generated using Faker.

    Args:
        session (Session): The session to use for adding the data to the database.

    Returns:
        None.
    """
    fake = Faker()

    # Generate fake sales for each house
    for house in session.query(House):
        buyer_details = fake.name()
        sale_price = fake.random_int(min=house.listing_price, max=int(house.listing_price * 1.5))
        date_of_sale = fake.date_between(start_date=house.date_of_listing, end_date='+1y')
        
        sale = Sale(
            buyer_details=buyer_details,
            sale_price=sale_price,
            date_of_sale=date_of_sale,
            house_id=house.id
        )
        session.add(sale)
    session.commit() 
    print('Sales populated.')

