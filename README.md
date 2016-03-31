# authcore
Python 3.5 #py3. PostgreSQL 9.4 #psql. Django 1.8 #django. Django REST framework 3.2 #drf. Authentication & Authorization API #authN #authZ.

AKA, the shit.

### authentication
AuthCore currently supports JWT as its primary means of authentication & verification. The following endpoints implement AuthCore's JWT functionality:

- `/jwt/authenticate/` — post `username` and `password` credentials to this endpoint to receive a JWT and the corresponding user's data.
- `/jwt/verify/` — post a JWT `token` to this endpoint to verify that it is valid and receive the corresponding user's data.
- `/jwt/refresh/` — post a JWT `token` to this endpoint to get a new JWT token and the corresponding user's data.

### development
Docker is used for all aspects of this project's development and deployment. Given a docker daemon to communicate with, simply do `docker-compose up -d` and your development infrastructure should come up.

The database will need to be primed before meaningful development can begin:
```bash
docker exec -it <authcoreID> bash
./manage.py makemigrations authcore
./manage.py migrate
./manage.py createsuperuser
```
