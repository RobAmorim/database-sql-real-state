from models.Office import Office
from models.Agent import EstateAgent
from models.Listing import House
from models.Sale import Sale
from models.Commission import Commission
from create import session
from datetime import datetime

#create Dummy Agent
for i in range(10):
    estate_agent = EstateAgent(
    name="Agent"+str(i),
    phone="004545435",
    email="abc@gmail.com"
    )
    session.add(estate_agent)

session.commit()
print('Agent Populated Dummy Data')

#Create Dummy Office
for i in range(10):
    office = Office(
    name="Ben Dummy"+str(i), 
    address="Minerva Street",
    )
    session.add(office)

session.commit()
print('Office Populated Dummy Data')


#Create Dummy House 
for i in range(10):
    house = House(
        seller_details="A",
        bedrooms=1+i,
        bathrooms=1+i,
        listing_price=4563475345,
        zip_code=423424,
        date_of_listing=datetime(2023, 4, 15),
        estate_agent_id=i,  # Assuming 10 estate agents exist
        office_id=i,  # Assuming 10 offices exist
    )
    session.add(house)

session.commit()
print('Listing Populated Dummy Data')

#CreateDummy Sales 
for i in range(10):
    sale = Sale(
        buyer_details="dfhsfhsdf",
        sale_price=346237423 - i,
        date_of_sale=datetime(2023, 4, 15+i),
        house_id=i
        )
    session.add(sale)
session.commit()
print('Listing Populated Dummy Data')



