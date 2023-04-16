from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import date
from models.Office import Office


def populate(session):

    # Create some offices
    office1 = Office(name='Office 1', location='Location 1')
    office2 = Office(name='Office 2', location='Location 2')
    office3 = Office(name='Office 3', location='Location 3')
    session.add_all([office1, office2, office3])
    session.commit()
    print('Office Populated')

    # Query the database
    users = session.query(Office).all()
    for user in users:
        print("Query offices", user.id, user.name)
