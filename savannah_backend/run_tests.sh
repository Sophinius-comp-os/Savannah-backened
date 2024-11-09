# Activate your virtual environment
source venv/Scripts/activate

# Run migrations
python manage.py migrate

# Run tests
coverage run manage.py test orders

# Generate coverage report
coverage report
