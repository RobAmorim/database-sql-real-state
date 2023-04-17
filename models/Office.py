from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from createConnection import Base


class Office(Base):
    """
    A class representing an office, with properties including an id, name, and address.

    Attributes:
        id (int): The unique identifier for the office.
        name (str): The name of the office.
        address (str): The address of the office.
    """
    __tablename__ = 'offices'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    address = Column(String)

    def __repr__(self):
        """
        Returns:
            str: A string representing the Office object and office name.
        """
        return f'<Office "{self.name}">'

