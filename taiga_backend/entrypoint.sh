#!/bin/sh

if [ -z $TAIGA_POSTGRES_HOST ];
then
    TAIGA_POSTGRES_HOST='postgres:5432'
fi

POSTGRES_HOST=`echo $TAIGA_POSTGRES_HOST | cut -f 1 -d :`
POSTGRES_PORT=`echo $TAIGA_POSTGRES_HOST | cut -f 2 -d :`

while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
  sleep 5
  echo "Waiting for $POSTGRES_HOST:$POSTGRES_PORT..."
done

python manage.py migrate --noinput
python manage.py loaddata initial_user
python manage.py loaddata initial_project_templates
python manage.py compilemessages
python manage.py collectstatic --noinput

supervisord -n
