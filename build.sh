#build the project
from daphne.cli import CommandLineInterface


echo "Building project..."
python3 -m pip install -r requirements.txt

echo "Make migrations..."
python3 manage.py makemigrations --noinput
python3 manage.py migrate --noinput

echo "Collect static..."
python3 manage.py collectstatic --noinput --clear

echo "UVICORNNNNNNNNNNNNNNNNNN..."
python -m uvicorn backend.asgi:application
