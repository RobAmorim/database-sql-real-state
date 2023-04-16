from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import date
from models.Sale import Sale
from models.Agent import EstateAgent
from models.Listing import House
from faker import Faker

def populate(session):

    fake = Faker()

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

    # Query the database
    # datas = session.query(Sale).all()
    # for data in datas:
    #     print("Sale", data.id)
