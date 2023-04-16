from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from models.Office import Office
from models.Agent import EstateAgent
from faker import Faker

def populate(session):

    # Create some offices
    fake = Faker()

    for i in range(10):
        office = Office(
        name=fake.company(), 
        address=fake.address(),
        )
        session.add(office)

    session.commit()
    print('Office Populated')

    # Query the database
    # datas = session.query(Office).all()
    # for data in datas:
    #     print("Query offices", data.name, data.address)
