# CS162 Database Application | Robson Silva

## Structure

`/models` contains all DB models using SQLAlchemy to define the tables.

`/populate` contains all the models to include fake data inside each table.

`/create.py` main application that creates the data base 

`/insert_data.py` insert the fake data inside the tables

`/query_data.py` query all the necessary informatiom.

`/query.py` define all functions to be query.

`/insert_dummy_data.py` insert dummy data inside the tables for test

`/test.py` contains the unit test code.

## Virtual Environment and run the app
Creating the virtualenv:

    $ virtualenv -p python3 venv

if it does not work, you can try this approach:

    $ python3 -m venv venv

Now, activate the activate the virtualenv. For Mac

    $ source venv/bin/activate

For **Windows** - [reference source:](https://stackoverflow.com/questions/8921188/issue-with-virtualenv-cannot-activate)

    $ venv\Scripts\activate

Installing the dependencies in the virtual environment:

    $ pip3 install -r requirements.txt

To create the database with the models:

	$ python3 create.py

To insert fake data to run the queries:

	$ python3 insert_data.py

To query the information:

	$ python3 query_data.py

To run the tests:

	$ python3 test.py

Closing the virtual env when finishing.

    $ deactivate 

