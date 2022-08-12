web: gunicorn JhonClinic.wsgi:application --log-file - --log-level debug
python manage.py makemigrations --noinput
python manage.py collectstatic --noinput
python manage.py migrate --noinput