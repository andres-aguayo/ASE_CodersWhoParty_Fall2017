#!/bin/bash
# make sure to run this in python3

python manage.py drop_db
python manage.py create_db
python manage.py db init
python manage.py db migrate
#python manage.py create_admin
python manage.py create_data
