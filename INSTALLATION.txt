This repository ought to be located in a dedicated 'weeabot' user's home directory at:
/home/weeabot/code/weeabot_site

it requires a dedicated project virtualenv (via virtualenvwrapper) at:
/home/weeeabot/.virtualenv/weeabot

Contents of virtualenv are described in weeabot/requirements.txt

Thus, the aboslute path of this README will be:
/home/weeabot/code/weeabot_site/README.txt

copy weeabot.uwsgi.ini and weeabot.uwsgi.override to /etc/init to support upstart daemon

softlink the nginx configuration via:
sudo ln -s /home/weeabot/code/weeabot_site/weeabot_nginx.conf /etc/nginx/sites-enabled/weeabot_nginx.conf

and then restart nginx
sudo /etc/init.d/nginx restart

You may have to remove the 'default' site enabled at /etc/nginx/sites-enabled/
