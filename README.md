## Table of contents
* [Technologies](#technologies)
* [Setup](#setup)
* [Loaddata](#loaddata)

## Technologies
Project is created with:
* Django
* Docker
* Postgresql

## Setup
To run this project:
```
$ sudo docker compose up --build
```

## Loaddata
To loaddata:
```
$ python3 manage.py loaddata ./scripts/client_db.json
$ python3 manage.py loaddata ./scripts/users_db.json
```
