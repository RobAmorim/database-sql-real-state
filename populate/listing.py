from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from models.Listing import House
from models.Agent import EstateAgent
from models.Office import Office
from faker import Faker 


def populate(session):
    fake = Faker()

    # Generate 50 fake houses
    for i in range(200):
        house = House(
            seller_details=fake.name(),
            bedrooms=fake.random_int(min=1, max=5),
            bathrooms=fake.random_int(min=1, max=3),
            listing_price=fake.random_int(min=100000, max=1000000),
            zip_code=fake.zipcode(),
            date_of_listing=fake.date_between(start_date='-1y', end_date='today'),
            estate_agent_id=fake.random_int(min=1, max=10),  # Assuming 10 estate agents exist
            office_id=fake.random_int(min=1, max=10),  # Assuming 10 offices exist
        )
        session.add(house)

    session.commit()
    print('Listing Populated')

    # Query the database
    # datas = session.query(House).all()
    # for data in datas:
    #     print("House", data.id)
