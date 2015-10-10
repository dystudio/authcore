# mafteka
מַפְתֵחַ — key. Django REST framework base. Django auth API. #drf #authN #authZ #pgsql.

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
To fire up the development server, execute the following:
```bash
./manage.py runserver
```
This should bring up the API on `localhost:8000`.
