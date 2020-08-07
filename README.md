# chit-fund-system
Value Chits (Chit-fund System)

Chit fund management application in django

Features

1) For Django 2.1 and Python 3.7
2) Modern virtual environments with pipenv
3) Styling with Bootstrap v4.1.3
4) Custom user model
5) username/password for log in/sign up instead of Django's default username/email/password pattern
6) Social authentication via django-allauth

First-time setup

1) Make sure Python 3.7x,Pipenv and PostgreSql are already installed.
2) Clone the repo and configure the virtualenv:

	$ git clone https://github.com/Patlavathsaikumar/chit-fund-system.git
	$ cd cfs
	$ pipenv install
	$ pipenv shell

Set up the initial migration for our custom user models in users and build the database.

	(cfs) $ python manage.py makemigrations users
	(cfs) $ python manage.py migrate

Create a superuser:
	
	(cfs) $ python manage.py createsuperuser

Confirm everything is working:

	(cfs) $ python manage.py runserver
	
Load the site at http://127.0.0.1:8000

