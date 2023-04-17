from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from models.Listing import House
from models.Agent import Agent
from models.Office import Office
from faker import Faker 


def populate(session, num):
    """
    Populates the house table with fake data generated using Faker.

    Args:
        session (Session): The session to use for adding the data to the database.
        num (int): The number of house records to generate.

    Returns:
        None.
    """
    fake = Faker()

    # Generate fake houses
    for i in range(num):
        house = House(
            seller_details=fake.name(),
            bedrooms=fake.random_int(min=1, max=5),
            bathrooms=fake.random_int(min=1, max=3),
            listing_price=fake.random_int(min=100000, max=1000000),
            zip_code=fake.zipcode(),
            date_of_listing=fake.date_between(start_date='-1y', end_date='today'),
            agent_id=fake.random_int(min=1, max=10),  # Assuming 10 estate agents exist
            office_id=fake.random_int(min=1, max=10),  # Assuming 10 offices exist
        )
        session.add(house)

    session.commit()
    print(f'{num} houses populated.')

