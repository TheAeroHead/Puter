# Puter
A shopping website for computer parts. Built with the Django Framework.

REQUIRED TOOLS: <br>
1. Installation of Python 3.7.2 or later. (should include sqlite3 and pip) <br>
2. Installation of Pip (likely installed with Python, if pip -V returns error run standalone installer) <br>
3. Installation of Pipenv (run pip install pipenv) <br>
4. Run pipenv shell before any pipenv install (else you won't install to the virtual environment) <br>
4. Installation of Django 2.1.5 or later. (run pipenv install django) <br>
5. Installation of PostgreSQL 11.2 or later. (use the enterpriseDB installer, will save a lot of setup headaches) <br>
6. Installation of pgAdmin4 (recommended and included in enterpriseDB installer) <br> 
7. Installation of psycopg2 package (run pipenv install psycopg2) <br>
8. Installation of Python library for Argon2 (run pipenv install django[argon2]) <br>
9. Installation of Stripe API (run pipenv install stripe) <br>

DEVELOPMENT SETUP: <br>
1. Clone the repository to the computer. (need to install pipenv in repository directory) <br>
2. Installation of all above tools (recommended to follow above order) <br>
3. pipenv shell to initialize virtual environment within project folder. Removes need to type python in front of manage.py and helps ensure no conflicts between python versions (if multiple installed). <br>
4. pgAdmin4 to check contents of database from GUI <br>
5. Make sure that all commands are run after initializing virtual environment with pipenv shell or will throw issues when you runserver. <br>
6. After installing PostgreSQL, run pgAdmin4 and login (password setup during install). Create new superuser datadmin for development purposes (preset authentication with this user in setttings.py)<br>
7. Create new database pUsers and give datadmin priviliges to use it if not already. <br>
8. Setup development server by running python manage.py makemigrations and python manage.py migrate <br>
9. Test app view by running python manage.py runserver <br>
10. Update development server by running python manage.py make migrations and python manage.py migrate
