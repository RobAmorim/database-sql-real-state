from create import session
from populate import office, agent, listing, sales


agent.populate(session)
office.populate(session)
listing.populate(session)
sales.populate(session)






