## Django application made with Python, psycopg2, Jinja and PostgreSQL.

## PROJECT DEPENDENCIES
- [Python 3 +](https://www.python.org/downloads/)
- [Visual Studio Code (IDE)](https://visualstudio.microsoft.com/)
- [PostgreSQL](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads)
- [Table Plus](https://tableplus.com/windows) or [pgAdmin 4](https://www.pgadmin.org/download/pgadmin-4-windows/)

## PROJECT SETUP
- Upon python installation, ensure that it is added to PATH
- Create a folder named YourProjectName
- Open Visual Studio Code and install the Django extension
- Navigate to the project directory in Visual Studio Code and open a terminal
- Enter:" pip install django " then restart the terminal
- Enter:" django-admin startproject YourProjectName "
- Make sure you are in the same directory or use " cd YourProjectName " if you created a folder before using the django-admin command
- Enter:" python manage.py startapp YourAppName "
- To test the server, run:" python manage.py runserver "
- Create a templates folder in the parent directory (same directory with your manage.py)
- Create an index.html

- To connect your app to django, navigate to your YourProjectName(Your Main folder) -> YourProjectName(Project Folder) -> settings.py
- In there, go to the INSTALLED APPS [] and add " 'YourAppName' "
- In the TEMPLATES [], add " 'templates' "

- In the same directory, go to urls.py and add " include " in the django.urls import
- Add the code:" path('',include('YourAppName.urls')), "

Your code should look like this:
```python

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('webapp.urls')),
]
```

- Now, copy the urls.py and add that to your YourAppName folder
- In that file, remove the admin import and the content of the urlpatterns like this:

```python
from django.urls import path

urlpatterns = [

]
```

## DB SETUP
- Configure your PostgreSQL management studio
- Create a database and take note of its name
- Create a terminal and pip install psycopg2 (for postgreSQL adapter)
- Also pip install django-environ (for .env)
- Create a .env file beside your settings.py and fill it with it like this (no single quotes):

```
SECRET_KEY=your_secret_key (can be seen in settings.py)
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
```
- Add this .env file to your gitignore if you are using git

Your settings.py should look like this:

```python
#settings.py

import environ
env = environ.Env()
environ.Env.read_env()

...some of the default code

# Your secret key
SECRET_KEY = env("SECRET_KEY")

...some of the default code

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env("DB_NAME"),
        'USER': env("DB_USER"),
        'PASSWORD': env("DB_PASSWORD"),
        'HOST': env("DB_HOST"),
        'PORT': env("DB_PORT"),
    }
}
```

- Get back to YourAppName folder and go to models.py and create your model (without ID)
- Open a terminal and make sure you are in the correct directory that contains manage.py or use " cd YourProjectName "
- Run the migrations by entering:" python manage.py makemigrations "
- Also enter:" python manage.py migrate "
- Check your database

## AND YOU ARE SET!
- For more information, visit this [link](https://stackpython.medium.com/how-to-start-django-project-with-a-database-postgresql-aaa1d74659d8)

## =================================================

# Django
======

Django is a high-level Python web framework that encourages rapid development
and clean, pragmatic design. Thanks for checking it out.

All documentation is in the "``docs``" directory and online at
https://docs.djangoproject.com/en/stable/. If you're just getting started,
here's how we recommend you read the docs:

* First, read ``docs/intro/install.txt`` for instructions on installing Django.

* Next, work through the tutorials in order (``docs/intro/tutorial01.txt``,
  ``docs/intro/tutorial02.txt``, etc.).

* If you want to set up an actual deployment server, read
  ``docs/howto/deployment/index.txt`` for instructions.

* You'll probably want to read through the topical guides (in ``docs/topics``)
  next; from there you can jump to the HOWTOs (in ``docs/howto``) for specific
  problems, and check out the reference (``docs/ref``) for gory details.

* See ``docs/README`` for instructions on building an HTML version of the docs.

Docs are updated rigorously. If you find any problems in the docs, or think
they should be clarified in any way, please take 30 seconds to fill out a
ticket here: https://code.djangoproject.com/newticket

To get more help:

* Join the ``#django`` channel on ``irc.libera.chat``. Lots of helpful people
  hang out there. `Webchat is available https://web.libera.chat/#django.

* Join the django-users mailing list, or read the archives, at
  https://groups.google.com/group/django-users.

* Join the `Django Discord community https://discord.gg/xcRH6mN4fa.

* Join the community on the `Django Forum` https://forum.djangoproject.com/.

To contribute to Django:

* Check out https://docs.djangoproject.com/en/dev/internals/contributing/ for
  information about getting involved.

To run Django's test suite:

* Follow the instructions in the "Unit tests" section of
  ``docs/internals/contributing/writing-code/unit-tests.txt``, published online at
  https://docs.djangoproject.com/en/dev/internals/contributing/writing-code/unit-tests/#running-the-unit-tests

Supporting the Development of Django
====================================

Django's development depends on your contributions.

If you depend on Django, remember to support the Django Software Foundation: https://www.djangoproject.com/fundraising/

