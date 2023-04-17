from create import session
from populate import office, agent, listing, sales


def populate_database(n_agent: int, n_office: int, n_listing: int, n_sales: int) -> None:
    """
    Populates the database with fake data.

    Args:
        n_agent (int): The number of fake agents to generate.
        n_office (int): The number of fake offices to generate.
        n_listing (int): The number of fake listings to generate.
        n_sales (int): The number of fake sales to generate.

    Returns:
        None
    """
    agent.populate(session, n_agent)
    office.populate(session, n_office)
    listing.populate(session, n_listing)
    sales.populate(session, n_sales)

# Populate the database with fake data
populate_database(n_agent=10, n_office=10, n_listing=200, n_sales=30)





