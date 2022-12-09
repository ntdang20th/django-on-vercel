#build the project
echo "Building project..."
python3 -m pip install -r requirements.txt

echo "DAPHNEEEEEEEEEEEE..."
python3 manage.py runworker channel_layer -v2
daphne backend.asgi:application --bind 0.0.0.0 -v2


echo "Make migrations..."
python3 manage.py makemigrations --noinput
python3 manage.py migrate --noinput

echo "Collect static..."
python3 manage.py collectstatic --noinput --clear

