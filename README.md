# authcore
authcore. Django auth API. Django REST framework base. #drf #authN #authZ #psql.

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
./manage.py syncdb
```

##### dev server
Fire up the development server:
```bash
./manage.py runserver
```
This should bring up the API on `localhost:8000`.
