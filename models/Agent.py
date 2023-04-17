from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from createConnection import Base

class Agent(Base):
    """
    A class representing an agent, with properties including an id, name, phone number, and email address.

    Attributes:
        id (int): The unique identifier for the agent.
        name (str): The name of the agent.
        phone (str): The phone number of the agent.
        email (str): The email address of the agent.
    """
    __tablename__ = 'agents'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    phone = Column(String)
    email = Column(String)

    def __repr__(self):
        """
        Returns:
            str: A string representing the Agent object and agent name.
        """
        return f'<Agent "{self.name}">'



