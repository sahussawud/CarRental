# CarRental

Car rental Website with Django Web Framework

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

Python 3.8.1 (Windows) download and install 

* [Python]( https://www.python.org ) - Python Official Site
* [PgAdmin]( https://www.pgadmin.org/ ) - PgAdmin Install & Create Database

Python 3.8.1 (MacOS) in Terminal from 
```
brew install python
```

### Installing

A step by step series of examples that tell you how to get a development env running
#### Automate step (All dependencies library will install)
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

Prerequisites Python Library
* Pillow 7.0.0
```
pip install Pillow
```
* psycopg2 2.8.4
```
pip install psycopg2
```


End with an example of getting some data out of the system or using it for a little demo

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


## Acknowledgments

* Car rental web-application
* Following business rule
