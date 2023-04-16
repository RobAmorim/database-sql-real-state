from create import session
from sqlalchemy import and_, extract
from models.Agent import EstateAgent
from models.Listing import House
from models.Office import Office
from models.Sale import Sale
from models.Commission import Commission
from sqlalchemy import func, desc, or_

def top_5_offices(month, year):
    results = session.query(Office, func.sum(Sale.sale_price))\
        .select_from(Sale)\
        .join(House)\
        .join(EstateAgent)\
        .join(Office)\
        .filter(and_(extract('month', Sale.date_of_sale) == month,
                     extract('year', Sale.date_of_sale) == year))\
        .group_by(Office)\
        .order_by(func.sum(Sale.sale_price).desc())\
        .limit(5)\
        .all()
    return results

def top_5_agents(month, year):
    results = session.query(EstateAgent, func.sum(Sale.sale_price))\
        .select_from(Sale)\
        .join(House)\
        .join(EstateAgent)\
        .join(Office)\
        .filter(and_(extract('month', Sale.date_of_sale) == month,
                     extract('year', Sale.date_of_sale) == year))\
        .group_by(EstateAgent)\
        .order_by(func.sum(Sale.sale_price).desc())\
        .limit(5)\
        .all()
    return results

def average_days_on_market(month, year):
    days_on_market = func.julianday(Sale.date_of_sale) - func.julianday(House.date_of_listing)
    avg_days_on_market = session.query(func.avg(days_on_market))\
        .select_from(Sale)\
        .join(House)\
        .filter(and_(extract('month', Sale.date_of_sale) == month,
                     extract('year', Sale.date_of_sale) == year))\
        .scalar()
    return avg_days_on_market

def average_price(month, year):
    avg_sell_price = session.query(func.avg(Sale.sale_price))\
        .select_from(Sale)\
        .filter(and_(extract('month', Sale.date_of_sale) == month,
                     extract('year', Sale.date_of_sale) == year))\
        .scalar()
    return avg_sell_price

def calculate_comssion(month, year): 
    montly_sales = session.query(Sale.id, Sale.sale_price, House)\
        .select_from(Sale)\
        .join(House)\
        .filter(and_(extract('month', Sale.date_of_sale) == month,
                     extract('year', Sale.date_of_sale) == year))\
        .all()
    
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
            estate_agent_id = sale.House.estate_agent_id
        )
        session.add(commission)

    session.commit()
    
    print('Commission per Agent')
    datas = session.query(Commission, EstateAgent)\
        .select_from(Commission)\
        .join(Sale)\
        .join(EstateAgent)\
        .group_by(EstateAgent)\
        .filter(and_(extract('month', Sale.date_of_sale) == month,
                     extract('year', Sale.date_of_sale) == year))\
        .all()
    
    for data in datas:
        print(data.EstateAgent.name, f'${data.Commission.commission_amount}') 