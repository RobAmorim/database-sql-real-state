from connection import session
from populate import office, agent, listing, sales

office.populate(session) 
agent.populate(session) 
listing.populate(session) 
sales.populate(session) 







