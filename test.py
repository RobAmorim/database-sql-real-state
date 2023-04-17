from unittest import TestCase
from unittest.mock import patch
from queries import top_5_offices, top_5_agents, average_days_on_market, average_price
from models.Office import Office
from models.Agent import Agent
from models.Listing import House
from models.Sale import Sale
from models.Commission import Commission
from datetime import datetime
from unittest import TestCase
from create import session
from sqlalchemy import and_, extract, func

#IMPORT DUMMY DATA
import insert_dummy_data

def test_top_5_offices():
    """
    Tests the top_5_offices function to ensure it returns the expected results.
    """

    # Retrieve the top 5 offices for the given month and year
    results = top_5_offices(4, 2023)

    # Assert that the length of the results is 5
    assert len(results) == 5

    # Assert that the first result has the correct name and sale price
    assert results[0][0].name == 'Ben Dummy0'
    assert results[0][1] == 346237421

    # Assert that the first result is an instance of the Office class and its sale price is an int
    assert isinstance(results[0][0], Office)
    assert isinstance(results[0][1], int)

    # Assert that the second result has the correct name and sale price
    assert results[1][0].name == 'Ben Dummy1'
    assert results[1][1] == 346237420

    # Assert that the second result is an instance of the Office class and its sale price is an int
    assert isinstance(results[1][0], Office)
    assert isinstance(results[1][1], int)

    # Print a success message if all assertions pass
    print("test_top_5_offices() | Successful")


test_top_5_offices() 

def test_top_5_agents():
    """
    Test the top_5_agents function using dummy data.
    """
    # Test the function with the dummy data
    results = top_5_agents(month=4, year=2023)

    # Check if the length of the results is 5
    assert len(results) == 5

    # Check the details of the first result
    assert results[0][0].name ==  'Agent0'
    assert results[0][1] ==  346237421
    assert isinstance(results[0][0], Agent)
    assert isinstance(results[0][1], int)

    # Check the details of the second result
    assert results[1][0].name ==  'Agent1'
    assert results[1][1] ==  346237420
    assert isinstance(results[1][0], Agent)
    assert isinstance(results[1][1], int)

    # Print a success message if all tests pass
    print('test_top_5_agents() | Successful')


test_top_5_agents() 

def test_average_days_on_market():
    """
    Tests the `average_days_on_market` function with dummy data.
    
    Checks that the function returns a float and that the calculated average number of days
    on the market is equal to the expected value.
    """
    
    results = average_days_on_market(month=4, year=2023)
    assert isinstance(results, float)
    assert results == 5.0
    
    print('test_average_days_on_market() | Successful')

test_average_days_on_market()

def test_average_price():  
    """Tests the average_price() function."""
    
    # Test the function with the dummy data
    results = average_price(month=4, year=2023)
    
    # Verify that the result is a float
    assert isinstance(results, float)
    
    # Verify that the result matches the expected value from dummy
    assert results == 346237418.5 

    # Print a success message if all tests pass
    print('test_average_price() | Successful')

test_average_price()




