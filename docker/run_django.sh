python /var/www/simple_api/manage.py makemigrations
python /var/www/simple_api/manage.py migrate
mkdir /var/www/simple_api/static
python /var/www/simple_api/manage.py fill_db
python /var/www/simple_api/manage.py collectstatic --noinput
while true; do sleep 1000; done