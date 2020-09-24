# Database webapp using python.

This project demonstrates a web application which has 3 parts.
1. A front-end website using html and css which takes input from the user:
   The input data consists of the user email-id and his/her height.
2. A database using postgresql:
   The user-input data is stored in the database if the email id entered by the user doesn't exist
   already in the database. Then, the average height is calculated. If the email id already exists 
   in the database, an error message is shown to the user.
3. Python code to send email: After average height is calculated, the following parameters are sent
   to the user's email id.
   1. User's height.
   2. Average height.
   3. Number of people participated in the survey.

## Prerequisites

Install flask and flask_sqlalchemy libraries using the below commands.

````
pip install flask

````

````
pip install flask_sqlalchemy

````

You should install postgresql and create a database in it. Give the correct username, password and name of database in webapp.py (line.no:21).

You can create the table for storing details in the database before running webappy.py using the below commands in python terminal.

````
from webapp import db

````

````
db.create_all()

````

Also insert your email id and password in line no. 15-16 in send_email.py

## Usage

Run the python file webapp.py. Use the commands below in any terminal.

````
python webapp.py

````
or if the python version is 3, use command.

````
python3 webapp.py

````
or you can also use any python IDE.

You will get a URL for your website in the terminal. Run the url in a browser.
