# drf-base
Django REST framework base. A simple project that I, or anyone else, can fork for a stable, working, browsable, tested, Django-based REST API.

AKA, the shit.

### development
##### dev server
To fire up the development server, execute the following:
```bash
./manage.py runserver
```
This should bring up the API on `localhost:8000`.

##### dev superuser
To create a superuser for the app, execute the following:
```bash
./manage.py createsuperuser
```
The user you craete here can be used to browse the API if you visit the API from a browser.
