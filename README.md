# Gorilla File 
### Web service to store file for 30 minutes with password protection support.

Steps to run this code in your device:
+ first clone this repo.
+ install virtualenv or use python env and create virtual environment.
+ next pip install requirement.txt file.
+ than run ```python manage.py shell``` in project root directory.
+ inside shell create database first my running ```db.create_all()```. This is only if you are using sqlite for development purposes.
+ you can set environment variables which are present in config.py file.
+ than run ```python manage.py runserver``` in terminal.
+ now server should be running at ```localhost:5000```
