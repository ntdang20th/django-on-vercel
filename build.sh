#build the project
echo "Building project..."
python3 -m pip install -r requirements.txt

echo "Make migrations..."
python3 manage.py makemigrations --noinput
python3 manage.py migrate --noinput

echo "Collect static..."
python3 manage.py collectstatic --noinput --clear

echo "Create superuser..."
try
  python3 manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', '123')"
catch
  print("Create failure!")
