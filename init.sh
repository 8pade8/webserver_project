sudo ln -s /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo rm -rf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo /etc/init.d/gunicorn restart
sudo gunicorn --bind='0.0.0.0:8080' hello:hello
sudo gunicorn --bind='0.0.0.0:8000' hello:hello