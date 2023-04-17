from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from createConnection import Base


class Commission(Base):
    """
    A class representing a commission, with properties including an id, commission amount, sale id, and agent id.

    Attributes:
        id (int): The unique identifier for the commission.
        commission_amount (int): The amount of commission.
        sale_id (int): The id of the sale associated with the commission.
        agent_id (int): The id of the agent associated with the commission.
    """
    __tablename__ = 'commissions'
    id = Column(Integer, primary_key=True)
    commission_amount = Column(Integer)
    sale_id = Column(Integer, ForeignKey('sales.id'))  
    agent_id = Column(Integer, ForeignKey('agents.id'))

    def __repr__(self):
        """
        Returns:
            str: A string representing the Commission object and commission name.
        """
        return f'<Commission "{self.name}">'

