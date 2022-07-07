# Scrapper

This project is to scrap the data from the given URL:
https://www.sebi.gov.in/sebiweb/other/OtherAction.do?doRecognisedFpi=yes&intmId=16

and the entire data is store into the database (POSTGRESQL)


# Setup the project:
1. activate the Virtual environment from the command for mac and ubuntu:
        source venv/bin/activate
2. Install the requirements.txt file to the virtual environment from the following command:
        pip install -r requirements.txt
3. After the installation part connect to the database configurations to the project in following files:

        session.py :- postgresql://(username):(password)@{host}:(port)/(db_name)

        alembic.py :- postgresql://(username):(password)@{host}:(port)/(db_name)
4. After the successful connection run command in terminal:

        alembic upgrade head

5. Run the uvicorn main:app --reload
6. open the url and hit the post api and then data is stored in database.

