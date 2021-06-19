echo "postgres:postgres" | chpasswd
cp /var/www/pg_hba.conf /etc/postgresql/12/main/pg_hba.conf
pg_ctlcluster 12 main start
psql -U postgres -f /var/www/upstart_django.sql