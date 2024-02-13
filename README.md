# Prueba técnica Infométrika

1. Virtual env
   python -m venv myenv
   source myenv/bin/activate

2. Install dependencies
   pip install djangorestframework
   pip install psycopg2

3. Database and migrations
   create database library_db
   using postgresql:
   CREATE DATABASE library_db;
   python manage.py migrate

### Database confguration in my_app.settings
