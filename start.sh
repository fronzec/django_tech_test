#!/bin/bash

python manage.py migrate --database=master
gunicorn urbvan.wsgi -b 0.0.0.0:8000