# hotel-room-booking-app:
![PyPI - Version](https://img.shields.io/pypi/v/Django?label=Django) ![PyPI - Version](https://img.shields.io/pypi/v/djangorestframework?label=djangorestframework)

___

# Quick Start

NOTE: The project uses Python 3.11, so need it installed first. It is recommended to use pyenv for installation.\
NOTE: Better to use PostgreSQL version > 10.0

**Here is a short instruction on how to quickly set up the project for development:**

+ Install poetry
+ git clone https://github.com/Dvaraz/hotel_room_booking_app.git
+ Install requierements:

+ $ poetry install
+ $ poetry shell

+ Install pre-commit hooks: $ pre-commit install
+ Create database in PostgreSQL
+ Add extension to all new creating databases (need for correct workig ExclusionConstraint) **psql -U postgres -h localhost -d template1 -c "CREATE EXTENSION btree_gist;"**
+ Add and setup .env file: $ cp .env.example .env -> edit .env
+ Initiate the database: $ poetry run python manage.py migrate
+ Manually create a superuser: $ python manage.py createsuperuser --email admin@gmail.com
+ Run the server: $ poetry run python manage.py runserver


