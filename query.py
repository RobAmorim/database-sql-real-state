from sqlalchemy import func, extract
from connection import session 
from models.Agent import EstateAgent 
from models.Office import Office
from models.Listing import House 
from models.Sale import Sale


def top_5_offices(month, year):
    query = session.query(Office.name, func.count(Sale.id).label('num_sales')).join(EstateAgent).join(Sale).filter(
        extract('month', Sale.date_of_sale) == month,
        extract('year', Sale.date_of_sale) == year
    ).group_by(Office.name).order_by(func.count(Sale.id).desc()).limit(5).all()
    return query



