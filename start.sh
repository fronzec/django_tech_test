#!/bin/sh

python manage.py migrate --database=master

python manage.py syncdb --noinput

echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'admin')" | python manage.py shell
echo "from django.contrib.auth.models import User; User.objects.create_superuser('urbvan', 'urbvan@example.com', 'pruebatecnica')" | python manage.py shell

exec "$@"