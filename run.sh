#!/bin/sh
python /code/manage.py makemigrations
python /code/manage.py migrate
python /code/manage.py loaddata hotel_data.json
python /code/manage.py runserver 0.0.0.0:8000
