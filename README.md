# Library API

![image](https://github.com/aortegaf/django.CRUD/assets/51802712/289df0ef-aab5-4dd6-b92d-1582f88ca290)

![image](https://github.com/aortegaf/django.CRUD/assets/51802712/1291ec7b-dde7-459f-b4b3-d2e4f42135e2)



### To run:

1. Create and activate virtual env

   - `python3 -m venv myenv`
   - `source myenv/bin/activate`

2. Install dependencies

   - `pip install -r requirements.txt`

3. Create **library_db** database _(Database configuration in my_app.settings)_

   - `sudo -u postgres psql`
   - `CREATE DATABASE library_db;`

4. Make migrations

   - `python3 manage.py makemigrations library_api`
   - `python3 manage.py migrate`

5. Run server
   - `python3 manage.py runserver`
