from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import date
from models.Agent import Agent
from faker import Faker


def populate(session, num):
    """
    Populates the agent table with fake data generated using Faker.

    Args:
        session (Session): The session to use for adding the data to the database.
        num (int): The number of agent records to generate.

    Returns:
        None.
    """
    # populate the agent table with faker
    fake = Faker()

    for i in range(num):
        agent = Agent(
            name=fake.name(),
            phone=fake.phone_number(),
            email=fake.email()
        )
        session.add(agent)

    session.commit()

    print(f'{num} agents populated.')

