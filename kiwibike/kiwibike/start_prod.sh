python manage.py migrate
gunicorn kiwibike.wsgi:application -k gevent -w 4 -b 0.0.0.0:5000 --reload
