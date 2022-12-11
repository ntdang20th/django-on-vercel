#build the project
echo "Building project..."
python3 -m pip install -r requirements.txt

echo "Make migrations..."
python3 manage.py makemigrations --noinput
python3 manage.py migrate --noinput

echo "Collect static..."
python3 manage.py collectstatic --noinput --clear

echo "DAPHNEEEEEEEEEEEE..."
#command: daphne -b 0.0.0.0 -p 8001 backend.asgi:application
#from daphne.cli import CommandLineInterface
#CommandLineInterface().run(('backend.asgi:application', '--bind', '0.0.0.0', '--port', '8001'))
subprocess.run(["daphne", "-b 0.0.0.0 -p 8001 backend.asgi:application"])