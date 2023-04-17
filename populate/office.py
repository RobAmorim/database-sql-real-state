from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from models.Office import Office
from models.Agent import Agent
from faker import Faker

def populate(session, num):
    """
    Populates the office table with fake data generated using Faker.

    Args:
        session (Session): The session to use for adding the data to the database.
        num (int): The number of office records to generate.

    Returns:
        None.
    """
    fake = Faker()

    # Generate fake offices
    for i in range(num):
        office = Office(
            name=fake.company(),
            address=fake.address(),
        )
        session.add(office)

    session.commit()
    print(f'{num} offices populated.')

