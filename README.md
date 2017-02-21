# footline_server
This runs the webserver for FootLine on Heroku and Development

# Installing
Clone this repository
Open the terminal in the repository folder
Requirements: Python 3, PostgreSQL 

Create a virtualenv with python3 
virtualenv -p python3
source env/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver# footline_server
