from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import date
from models.Listing import House
from models.Agent import EstateAgent


def populate(session):
    agent1 = session.query(EstateAgent).filter_by(name='Agent 1').first()
    agent2 = session.query(EstateAgent).filter_by(name='Agent 2').first()
    agent3 = session.query(EstateAgent).filter_by(name='Agent 3').first()
    agent4 = session.query(EstateAgent).filter_by(name='Agent 4').first()
    agent5 = session.query(EstateAgent).filter_by(name='Agent 5').first()
    agent6 = session.query(EstateAgent).filter_by(name='Agent 6').first()

    # List some Houses
    house1 = House(seller_name='Seller 1', num_bedrooms=3, num_bathrooms=2, listing_price=1000000, zip_code='12345', date_of_listing=date(2023, 1, 1), estate_agent_id=agent1.id)
    house2 = House(seller_name='Seller 2', num_bedrooms=4, num_bathrooms=2, listing_price=1500000, zip_code='23456', date_of_listing=date(2023, 1, 15), estate_agent_id=agent2.id)
    house3 = House(seller_name='Seller 3', num_bedrooms=2, num_bathrooms=1, listing_price=500000, zip_code='34567', date_of_listing=date(2023, 2, 1), estate_agent_id=agent3.id)
    house4 = House(seller_name='Seller 4', num_bedrooms=5, num_bathrooms=3, listing_price=2000000, zip_code='45678', date_of_listing=date(2023, 2, 15), estate_agent_id=agent4.id)
    house5 = House(seller_name='Seller 5', num_bedrooms=3, num_bathrooms=2, listing_price=800000, zip_code='56789', date_of_listing=date(2023, 3, 1), estate_agent_id=agent5.id)
    house6 = House(seller_name='Seller 6', num_bedrooms=4, num_bathrooms=3, listing_price=1800000, zip_code='67890', date_of_listing=date(2023, 3, 15), estate_agent_id=agent6.id)
    session.add_all([house1, house2, house3, house4, house5, house6])
    session.commit()
    print('Listing Populated')

    # Query the database
    users = session.query(House).all()
    for user in users:
        print("House", user.id)
