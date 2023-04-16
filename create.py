from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from createConnection import Base
from models.Office import Office
from models.Agent import EstateAgent
from models.Listing import House
from models.Sale import Sale
from models.Commission import Commission

# Initializing
engine = create_engine("sqlite:///real_estate.db", echo=False)

# Drop tables
Base.metadata.drop_all(engine)

# Create tables
Base.metadata.create_all(engine)

# Creating a session
Session = sessionmaker(bind=engine)
session = Session()
