release: python manage.py makemigrrations --no-input
release : python manage.py migrate --no-input

web: gunicorn WebDjango.wsgi 