create user django_user with password '1234567890';
alter role django_user set client_encoding to 'utf8';
alter role django_user set default_transaction_isolation to 'read committed';
alter role django_user set timezone to 'UTC';
create database django_db owner django_user;