from faker import Faker
from datetime import datetime, timedelta
from random import randint
from sqlalchemy.orm import sessionmaker
from others.realState import Office, Agent, Listing, Commission, Sale, engine

func = randint

# create a faker object
fake = Faker()

# create a session
Session = sessionmaker(bind=engine)
session = Session()

# create offices
for i in range(5):
    office = Office(name=fake.company(), city=fake.city(), state=fake.state_abbr(), zip_code=fake.zipcode())
    session.add(office)

# create agents
for i in range(20):
    agent = Agent(name=fake.name(), email=fake.email(), phone_number=fake.phone_number(),
                  office=session.query(Office).order_by(func.random()).first())
    session.add(agent)

# create listings
for i in range(100):
    listing = Listing(seller_details=fake.name(), bedrooms=randint(1, 5), bathrooms=randint(1, 4),
                      listing_price=randint(100000, 1000000), zip_code=fake.zipcode(),
                      date_of_listing=fake.date_between(start_date='-2y', end_date='today'),
                      agent=session.query(Agent).order_by(func.random()).first(),
                      office=session.query(Office).order_by(func.random()).first())
    session.add(listing)

# create sales
for i in range(50):
    listing = session.query(Listing).filter_by(sold=0).order_by(func.random()).first()
    if listing:
        listing.sold = 1
        sale = Sale(buyer_details=fake.name(), sale_price=listing.listing_price * randint(90, 110) / 100,
                    date_of_sale=listing.date_of_listing + timedelta(days=randint(30, 90)),
                    agent=listing.agent, office=listing.office, listing=listing)
        session.add(sale)

# commit the changes
session.commit()
