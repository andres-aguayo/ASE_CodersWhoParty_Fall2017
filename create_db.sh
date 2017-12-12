#!/bin/bash
# make sure to run this in python3

rm -r migrations
python3 manage.py drop_db
python3 manage.py create_db
python3 manage.py db init
python3 manage.py db migrate
python3 manage.py create_admin
python3 manage.py create_data
