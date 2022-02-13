# OCR_P10

# Create a virtual environment to isolate our package dependencies locally
python3 -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`

# Install all needed dependencies
pip3 install -r requirements.txt

# Make migrations
python3 manage.py makemigrations

# Create SuperUser
python3 manage.py createsuperuser

# Migrate
python3 manage.py migrate

# Run Server
python3 manage.py runserver
