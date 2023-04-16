from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import date
from models.Agent import EstateAgent
from faker import Faker


def populate(session):

    # Create some offices
    fake = Faker()

    for i in range(10):
        estate_agent = EstateAgent(
        name=fake.name(),
        phone=fake.phone_number(),
        email=fake.email()
        )
        session.add(estate_agent)

    session.commit()

    print('Agent Populated')

    #Query the database
    # datas = session.query(EstateAgent).all()
    # for data in datas:
    #     print("Query Agents", data.id, data.name)
