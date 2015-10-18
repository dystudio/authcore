# authcore
Python 3.5 #py3. PostgreSQL 9.4 #psql. Django 1.8 #django. Django REST framework 3.2 #drf. Authentication & Authorization API #authN #authZ.

AKA, the shit.

### development
##### dev database
For now, the app is only configured to be backed with PostgreSQL. Before firing anything up, do the following:
```bash
./scripts/pgdev.sh
```

##### dev syncdb
Prime the database for development:
```bash
./manage.py makemigrations
./manage.py migrate
./manage.py createsuperuser
```

##### dev server
Fire up the development server:
```bash
./manage.py runserver
```
This should bring up the API on `localhost:8000`.
