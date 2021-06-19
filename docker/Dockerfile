FROM ubuntu:20.04
ENV DEBIAN_FRONTEND noninteractive 

# PREPARE LINUX PROGRAMMS
RUN apt-get update
RUN apt-get install -y mc
RUN apt-get install -y htop
RUN apt-get install -y curl
RUN apt-get install -y language-pack-ru
RUN apt-get install -y language-pack-en

# PREPARE VUE
RUN apt-get install -y npm

# PREPARE PYTHON
RUN apt-get install -y python3.8
RUN apt-get install -y python3.8-distutils
RUN apt-get install -y python3-dev
RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
RUN python3.8 get-pip.py
RUN apt-get install -y python3-venv
RUN ln -s /usr/bin/python3.8 /usr/bin/python

# INSTALL VUE
RUN npm install vue

# INSTALL NGINX
RUN apt-get install -y nginx
RUN echo "daemon off;" >> /etc/nginx/nginx.conf
RUN sed -i "0,/nginx/s/nginx/docker-nginx/i" /usr/share/nginx/html/index.html

# PREPARE API
WORKDIR /var/www/
COPY simple_api /var/www/simple_api
RUN pip install -r /var/www/simple_api/requirements.txt
WORKDIR /var/www/simple_api
RUN pip install psycopg2-binary


# START VUE
COPY vue_app /var/www/vue_app
WORKDIR /var/www/vue_app/
RUN npm install
RUN npm run build

# COPY BOOTSTRAP TO PV3
COPY bootstrap-4.1.3-dist/css /var/www/vue_app/dist/css
COPY jquery-3.6.0.min.js /var/www/vue_app/dist/js/jquery-3.6.0.min.js
COPY bootstrap-4.1.3-dist/js /var/www/vue_app/dist/js

# UPSTART NGINX
COPY uwsgi_params /var/www/
COPY simple_api.conf /var/www/
COPY vue_nginx.conf /var/www/
COPY data.json /var/www/data.json
RUN ln -s /var/www/simple_api.conf /etc/nginx/sites-enabled/
RUN ln -s /var/www/vue_nginx.conf /etc/nginx/sites-enabled/

# START PSQL
RUN apt-get install -y postgresql

# OPEN PORT FOR APACHE2
EXPOSE 80

# INSTALL UWSGI
RUN pip install uwsgi

# COPY CONFs
COPY run_simple_uwsgi.sh /var/www/run_simple_uwsgi.sh
COPY run_psql.sh /var/www/run_psql.sh
COPY run_django.sh /var/www/run_django.sh
COPY upstart_django.sql /var/www/upstart_django.sql
COPY pg_hba.conf /var/www/pg_hba.conf

# RUN ALL BINARIES AND SERVICES
CMD nginx & . /var/www/run_simple_uwsgi.sh & . /var/www/run_psql.sh ; . /var/www/run_django.sh