from create import session
from sqlalchemy import and_, extract
from models.Agent import Agent
from models.Listing import House
from models.Office import Office
from models.Sale import Sale
from models.Commission import Commission
from sqlalchemy import func, desc, or_

def top_5_offices(month, year):
    """
    Queries the database for the top 5 offices by sales revenue in a given month and year.

    Args:
        month (int): The month to query (1-12).
        year (int): The year to query.

    Returns:
        List[Tuple[Office, int]]: A list of tuples, where each tuple contains an Office object and the total
        sales revenue for that office in the specified month and year. The list is sorted in descending order
        by sales revenue, and is limited to the top 5 offices.
    """
    results = session.query(Office, func.sum(Sale.sale_price))\
        .select_from(Sale)\
        .join(House)\
        .join(Agent)\
        .join(Office)\
        .filter(and_(extract('month', Sale.date_of_sale) == month,
                     extract('year', Sale.date_of_sale) == year))\
        .group_by(Office)\
        .order_by(func.sum(Sale.sale_price).desc())\
        .limit(5)\
        .all()
    return results


def top_5_agents(month, year):
    """
    Retrieves the top 5 agents in terms of sales revenue for a given month and year.

    Args:
        month (int): The month to filter sales by.
        year (int): The year to filter sales by.

    Returns:
        A list of tuples, where each tuple contains an Agent object and the total sale revenue for that agent for
        the given month and year. The list is sorted in descending order by sale revenue, and contains a maximum of
        5 tuples.
    """
    results = session.query(Agent, func.sum(Sale.sale_price))\
        .select_from(Sale)\
        .join(House)\
        .join(Agent)\
        .join(Office)\
        .filter(and_(extract('month', Sale.date_of_sale) == month,
                     extract('year', Sale.date_of_sale) == year))\
        .group_by(Agent)\
        .order_by(func.sum(Sale.sale_price).desc())\
        .limit(5)\
        .all()
    return results


def average_days_on_market(month, year):
    """
    Calculates the average number of days a house is on the market before being sold in a given month and year.

    Args:
        month (int): The month for which the calculation is done (1-12).
         year (int): The year for which the calculation is done.

    Returns:
        float: The average number of days a house is on the market before being sold in the given month and year.
    """
    days_on_market = func.julianday(Sale.date_of_sale) - func.julianday(House.date_of_listing)
    avg_days_on_market = session.query(func.avg(days_on_market))\
        .select_from(Sale)\
        .join(House)\
        .filter(and_(extract('month', Sale.date_of_sale) == month,
                     extract('year', Sale.date_of_sale) == year))\
        .scalar()
    return avg_days_on_market


def average_price(month, year):
    """
    Returns the average sale price of all houses sold in a given month and year.

    Args:
        month (int): The month of interest.
        year (int): The year of interest.

    Returns:
        float: The average sale price of all houses sold in the given month and year.
    """
    avg_sell_price = session.query(func.avg(Sale.sale_price))\
        .select_from(Sale)\
        .filter(and_(extract('month', Sale.date_of_sale) == month,
                     extract('year', Sale.date_of_sale) == year))\
        .scalar()
    return avg_sell_price


def calculate_comssion(month, year): 
    """
    Calculates and adds the commission for each agent for the given month and year.

    Args:
    month (int): The month for which to calculate the commission.
    year (int): The year for which to calculate the commission.

    Returns:
    None
    """
    # Get all sales for the given month and year
    montly_sales = session.query(Sale.id, Sale.sale_price, House)\
        .select_from(Sale)\
        .join(House)\
        .filter(and_(extract('month', Sale.date_of_sale) == month,
                     extract('year', Sale.date_of_sale) == year))\
        .all()
    
    # Calculate and add the commission for each sale
    for sale in montly_sales:
        commission_amount = 0 
        if sale.sale_price < 100000:
            commission_amount = sale.sale_price * 0.1

        elif sale.sale_price < 200000:
            commission_amount = sale.sale_price * 0.075

        elif sale.sale_price < 500000:
            commission_amount = sale.sale_price * 0.06

        elif sale.sale_price < 1000000:
            commission_amount = sale.sale_price * 0.05
        else:
            commission_amount = sale.sale_price * 0.04

        commission = Commission (
            commission_amount = commission_amount,
            sale_id = sale.id,
            agent_id = sale.House.agent_id
        )
        session.add(commission)

    session.commit()
    
    # Display the commission per agent
    print('Commission per Agent')
    datas = session.query(Commission, Agent)\
        .select_from(Commission)\
        .join(Sale)\
        .join(Agent)\
        .group_by(Agent)\
        .filter(and_(extract('month', Sale.date_of_sale) == month,
                     extract('year', Sale.date_of_sale) == year))\
        .all()
    
    for data in datas:
        print(data.Agent.name, f'${data.Commission.commission_amount}')
