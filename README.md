# CarRental

Car rental application with Django Web Framework

* [https://car-rental-demo-app.herokuapp.com](https://car-rental-demo-app.herokuapp.com) - Demo Website

* [โปรเจกต์ร้านเช่ารถ กับ Django Web Framework](https://poundsahussawud.medium.com/%E0%B9%82%E0%B8%9B%E0%B8%A3%E0%B9%80%E0%B8%88%E0%B9%87%E0%B8%84%E0%B8%A3%E0%B9%89%E0%B8%B2%E0%B8%99%E0%B9%80%E0%B8%8A%E0%B9%88%E0%B8%B2%E0%B8%A3%E0%B8%96-%E0%B8%81%E0%B8%B1%E0%B8%9A-django-web-framework-4e2788e1d7c2) - Read My Article


### Prerequisites

* [Python]( https://www.python.org ) - Python Official Site
* [PgAdmin]( https://www.pgadmin.org/ ) - PgAdmin Install & Create Database

Python 3.8.1 (MacOS) in Terminal from 
```
brew install python
```
Set up databse you prefer eg. MySQLite, Postgres

### Installing

```
pip install -r requirements.txt
```

#### Manual step

Django install

```
python3 -m pip install Django
```

And Check django-admin version to check Django work

```
django-admin --version
```

create environment for project

```
python3 -m venv env
```

activate python environment from env

```
/env/Scrips/activate
```

## Running the tests

Explain how to run the automated tests for this system

make Model migration for prepare to migrate Model to PostgreSQL
```
python3 manage.py makemigrations
```
Migrate model
```
python3 manage.py migrate
```
runserver
```
python3 manage.py runserver
```
create admin to access superuser
```
python3 manage.py createsuperuser
```


## Built With

* [Django](https://getbootstrap.com/) - The web back-end framework used
* [Boostrap3](https://getbootstrap.com/) - The web front-end framework end
* [PgAdmin](https://www.pgadmin.org/) - Used to generate RSS Feeds



## Authors

* **Sahussawud Khunruksa** - *Initial work* - 

