from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import date
from models.Sale import Sale
from models.Agent import EstateAgent
from models.Listing import House

def populate(session):

    agent1 = session.query(EstateAgent).filter_by(name='Agent 1').first()
    agent2 = session.query(EstateAgent).filter_by(name='Agent 2').first()

    house1 = session.query(House).filter_by(id=1).first()
    house2 = session.query(House).filter_by(id=2).first()

    # Create some offices
    sale1 = Sale(buyer_name='Mary Jane', sale_price=1000000.00, date_of_sale=date(2023, 4, 10), estate_agent_id=agent1.id, house_id=house1.id)
    sale2 = Sale(buyer_name='Steve Rogers', sale_price=500000.00, date_of_sale=date(2023, 4, 11), estate_agent_id=agent2.id, house_id=house2.id)
    session.add_all([sale1, sale2])
    session.commit()
    print('Sales Populated')

    # Query the database
    users = session.query(Sale).all()
    for user in users:
        print("Sale", user.id)
