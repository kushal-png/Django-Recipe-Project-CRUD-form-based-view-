# Create Virtual environment
python -m virtualenv venv

# On Windows
venv\Scripts\activate

# Install Dependencies
pip install -r requirements.txt

# run
python manage.py migrate
python manage.py runserver
