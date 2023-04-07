
# adduser taki

ssh root@your_server_ip

adduser taki

usermod -aG sudo taki
su - taki

## Setting Up a Basic Firewall
sudo ufw app list
sudo ufw allow OpenSSH
sudo ufw enable # pres y after 
sudo ufw status 


1
sudo apt-mark hold pyhton # to exclude python from beiing upgraded

# sudo apt update
# sudo apt upgrade

sudo apt-get update
sudo apt-get install python3-pip python3-dev libpq-dev postgresql postgresql-contrib nginx

# sudo -u postgres psql

CREATE DATABASE crm_db;
CREATE USER octopus WITH PASSWORD 'miyou0209';
ALTER ROLE octopus SET client_encoding TO 'utf8';
ALTER ROLE octopus SET default_transaction_isolation TO 'read committed';
ALTER ROLE octopus SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE crm_db TO octopus;
\q

# CONFIGURE DJANGO
sudo -H pip3 install --upgrade pip
sudo -H pip3 install virtualenv
virtualenv venv

source venv/bin/activate

## clone the repo 

pip install -r requirements.txt
## add local_settings.py

sudo nano local_settings.py


# SECURITY WARNING: don't run with debug turned on in production!
SECRET_KEY = 'ir35_cazgolfmmt++=9i_1escks$hck!2lgot@enblen%6n7kt&g!'
DEBUG = False

ALLOWED_HOSTS = ['178.62.41.8' ,'www.crm.octopus-consulting.com.com', 'crm.octopus-consulting.com.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': "crm_db",
        'USER': "octopus",
        'PASSWORD': "miyou0209",
        'HOST': "localhost",
        'PORT': "5432",
    }
}

python manage.py makemigrations

# ERROR cairo
no library called "libcairo-2" was founds

# solution 

sudo apt-get install libpangocairo-1.0-0
.
python manage.py makemigrations
python manage.py migrate


sudo ufw allow 8000

gunicorn --bind 0.0.0.0:8000 config.wsgi

# Gunicorn configuration

sudo nano /etc/systemd/system/abds.socket

[Unit]
Description=gunicorn socket

[Socket]
ListenStream=/run/abds.sock

[Install]
WantedBy=sockets.target


sudo nano /etc/systemd/system/abds.service


[Unit]
Description=gunicorn daemon
Requires=abds.socket
After=network.target

[Service]
User=taki
Group=www-data
WorkingDirectory=/home/taki/abds/new_octopus_abds
ExecStart=/home/taki/abds/venv/bin/gunicorn \
          --access-logfile - \
          --workers 3 \
          --bind unix:/run/abds.sock \
          config.wsgi:application

[Install]
WantedBy=multi-user.target


sudo systemctl start abds.socket
sudo systemctl enable abds.socket

# possible command check errors sudo journalctl -u abds.socket

sudo systemctl daemon-reload
sudo systemctl restart abds

# NGINX CONFIGURATION

sudo nano /etc/nginx/sites-available/abds

    location / {
        proxy_pass http://crm.octopus-consulting.com;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
server {
    listen 80;
    server_name 178.62.41.8 abdoptic.com www.abdoptic.com ;
    location = /favicon.ico { access_log off; log_not_found off; }

    location /media/ {
        root /home/taki/abds/abds;    
    }
    location /static/ {
        root /home/taki/abds/abds;    
    }
    location /assets/ {
        root /home/taki/abds/abds;    
    }
    location / {
        include proxy_params;
        proxy_pass http://unix:/run/abds.sock;
    }
}

sudo ln -s /etc/nginx/sites-available/abds /etc/nginx/sites-enabled

sudo nginx -t
#
sudo systemctl restart nginx
sudo ufw delete allow 8000
sudo ufw allow 'Nginx Full'

# Possible command sudo tail -F /var/log/nginx/error.log

#migrate sqlite to postgresql if it have to

1* 
python manage.py shell
from django.contrib.contenttypes.models import ContentType
ContentType.objects.all().delete()
  
python manage.py loaddata fixture/whole.json ,

# command

sudo systemctl reload nginx
sudo systemctl restart crm

add allowwed hosts

# Custom domaine
@  A Record  178.62.41.8
www  CNAME  socialfacilite.com

ALLOWED_HOSTS = ['165.227.224.201' ,'www.socialfacilite.com', 'socialfacilite.com']

sudo nano /etc/nginx/sites-available/social

server {
    listen: 80;
    server_name 165.227.224.201 www.socialfacilite.com socialfacilite.com;
}

sudo systemctl restart nginx 
sudo systemctl restart crm

# Configuration SSL

 sudo nano /etc/nginx/nginx.conf
add 
client_max_body_size 20M;

# Add SSL

sudo apt install certbot python3-certbot-nginx

sudo nano /etc/nginx/sites-available/social

check  -> sudo nginx -t

sudo systemctl reload nginx
sudo ufw status

sudo ufw allow 'Nginx Full'
sudo ufw delete allow 'Nginx HTTP'

sudo certbot --nginx -d abdoptic.com -d www.abdoptic.com

sudo systemctl status certbot.timer
sudo certbot renew --dry-run

# print errors 

sudo cat /var/log/syslog

sudo tail -30 /var/log/nginx/error.log

