Hi Fatmug!

This is my submission for the assessment that was given to me on 29th of April.
I have attached all the required documents.
To understand the API's refer to 'API_Documentation.txt', I have documented every API thoroughly.

## ✨ Setup and Demo

Switch to the master branch after cloning the repository:

```sh
git checkout master
```

Create a new virtual environment and activate

```sh
python3 -m venv .env
. .env/bin/activate
```
install the required packages from 'requirements.txt' file.

```sh
pip install -r requirements.txt
```

Once all the packages are installed move to the 'manage.py' file location and run the  following commands

```sh
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser #follow the commands to fill details
python manage.py runserver
```
After starting the django server you are ready to test the APIs.

## ✨ Model checks and Admin Access

To access the admin panel use "/admin" after the default localhost url and enter the username and password used for creating the superuser.
