from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import date
from models.Agent import EstateAgent
from models.Office import Office


def populate(session):
    office1 = session.query(Office).filter_by(name='Office 1').first()
    office2 = session.query(Office).filter_by(name='Office 2').first()
    office3 = session.query(Office).filter_by(name='Office 3').first()

    # Create some offices
    agent1 = EstateAgent(name='Agent 1', email='agent1@example.com', office_id=office1.id)
    agent2 = EstateAgent(name='Agent 2', email='agent2@example.com', office_id=office1.id)
    agent3 = EstateAgent(name='Agent 3', email='agent3@example.com', office_id=office2.id)
    agent4 = EstateAgent(name='Agent 4', email='agent4@example.com', office_id=office2.id)
    agent5 = EstateAgent(name='Agent 5', email='agent5@example.com', office_id=office3.id)
    agent6 = EstateAgent(name='Agent 6', email='agent6@example.com', office_id=office3.id)
    session.add_all([agent1, agent2, agent3, agent4, agent5, agent6])
    session.commit()
    print('Agent Populated')

    #Query the database
    users = session.query(EstateAgent).all()
    for user in users:
        print("Query Agents", user.id, user.name)
