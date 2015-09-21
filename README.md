# drf-base
Django REST framework base. A simple project that I, or anyone else, can fork for a stable, working, browsable, tested, Django-based REST API.

AKA, the shit.

### development
##### dev database
For now, the app is only configured to be backed with sqlite3. Before firing anything up, do the following:
```bash
./manage.py migrate
```
This will initialize and synchronize a sqlite3 database for development.

##### dev superuser
To create a superuser for the app, execute the following:
```bash
./manage.py createsuperuser
```
The user you craete here can be used to browse the API if you visit the API from a browser.

##### dev server
To fire up the development server, execute the following:
```bash
./manage.py runserver
```
This should bring up the API on `localhost:8000`.


