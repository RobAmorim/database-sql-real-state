from unittest import TestCase
from unittest.mock import patch
from queries import top_5_offices, top_5_agents, average_days_on_market, average_price
from models.Office import Office
from models.Agent import EstateAgent
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

    results = top_5_offices(4, 2023)

    assert len(results) == 5
    assert results[0][0].name ==  'Ben Dummy0'
    assert results[0][1] ==  346237421
    assert isinstance(results[0][0], Office)
    assert isinstance(results[0][1], int)

    assert results[1][0].name ==  'Ben Dummy1'
    assert results[1][1] ==  346237420
    assert isinstance(results[1][0], Office)
    assert isinstance(results[1][1], int)

    print("test_top_5_offices() | Successful") 

test_top_5_offices() 

def test_top_5_agents():  
    # Test the function with the dummy data
    results = top_5_agents(month=4, year=2023)
    assert len(results) == 5
    assert results[0][0].name ==  'Agent0'
    assert results[0][1] ==  346237421
    assert isinstance(results[0][0], EstateAgent)
    assert isinstance(results[0][1], int)

    assert results[1][0].name ==  'Agent1'
    assert results[1][1] ==  346237420
    assert isinstance(results[1][0], EstateAgent)
    assert isinstance(results[1][1], int)

    print('test_top_5_agents() | Successful')

test_top_5_agents() 

def test_average_days_on_market():  
    
    results = average_days_on_market(month=4, year=2023)
    assert isinstance(results, float)
    assert results == 5.0

    print('test_average_days_on_market() | Successful')

test_average_days_on_market()

def test_average_price():  
    
    results = average_price(month=4, year=2023)
    assert isinstance(results, float)
    assert results == 346237418.5 

    print('test_average_price() | Successful')


test_average_price()



