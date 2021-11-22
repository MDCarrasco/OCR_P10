# OCR_P10

# Create the project directory
mkdir tutorial
cd tutorial

# Create a virtual environment to isolate our package dependencies locally
python3 -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`

# Install Django and Django REST framework into the virtual environment
pip install django
pip install djangorestframework

# Set up a new project with a single application
django-admin startproject P10 .  # Note the trailing '.' character
cd tutorial
django-admin startapp SoftDesk
cd ..

# Make migrations
python3 manage.py makemigrations

# Create SuperUser
python3 manage.py createsuperuser

# Migrate
python3 manage.py migrate

# Run Server
python3 manage.py runserver
