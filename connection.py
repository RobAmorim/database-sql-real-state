from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.Agent import EstateAgent, Base as AgentBase
from models.Listing import House, Base as ListingBase 
from models.Sale import Sale, Base as SaleBase 
from models.Office import Office, Base as OfficeBase

# Initializing
engine = create_engine('sqlite:///real_estate.db', echo=True)

# Drop tables
AgentBase.metadata.drop_all(engine)
OfficeBase.metadata.drop_all(engine)
SaleBase.metadata.drop_all(engine)
ListingBase.metadata.drop_all(engine)

# Create tables
AgentBase.metadata.create_all(engine)
OfficeBase.metadata.create_all(engine)
SaleBase.metadata.create_all(engine)
ListingBase.metadata.create_all(engine)

# Creating a session
Session = sessionmaker(bind=engine)
session = Session()



