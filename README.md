## Django application made with Python, PostgreSQL.

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
'''python

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('webapp.urls')),
]

'''

- Now, copy the urls.py and add that to your YourAppName folder
- In that file, remove the admin import and the content of the urlpatterns like this:

'''python
from django.urls import path

urlpatterns = [

]

'''

## DB SETUP
- Configure your PostgreSQL management studio
- Create a database and take note of its name

## AND YOU ARE SET!
- For more information, visit this [link](https://stackpython.medium.com/how-to-start-django-project-with-a-database-postgresql-aaa1d74659d8)
