Hi Fatmug!

This is my submission for the assessment that was given to me on 29th of April.

I have attached all the required documents.

To understand the API's refer to API_Documentation.txt, I have documented every API thoroughly.

To setup the application, clone this repo in a virtual environment and install the required packages from
'requirements,txt' file  using the following command.

pip install -r requirements.txt

Once all the  packages are installed move to the manage.py file location and run the  following commands

python manage.py migrate

python manage.py createsuperuser

python manage.py runserver

Enter a valid username, password and a valid  email ID when running "python manage.py createsuperuser" command.

To access the admin panel use "/admin" after  the  default  localhost url and enter the  username and password.

Create a new user without admin access to test the API's!
