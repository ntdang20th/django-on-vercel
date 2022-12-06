#build the project
echo "Building project..."
python3 -m pip install -r requirements.txt

echo "Make migrations..."
python3 manage.py makemigrations --noiput
python3 manage.py migrate --noiput

echo "Collect static..."
python3 manage.py collectstatic --noiput --clear