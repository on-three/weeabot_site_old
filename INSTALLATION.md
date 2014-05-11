#Overview
Okay. weeabot is currently the following:
* An IRC bot that supports japanese word lookups
* A Django backend that records lookups to a database and can present them via a web page.

I've configured this repository to match the configuration I'd like to see on a web server that runs both the above services. For this reason, I don't support simple pip installation anymore. This doesn't seem to agree with django installations.

Installation is currently as described below:

#Requirements
So far I've only run on LinuxMint16, but this should all run on any system with python, if it can satisfy requirements.txt.


##virtualenv
Make sure you can create and activate/deactivate python virtual environments via virtualenvwrapper
```
sudo apt-get install virtualenvwrapper
```
You'll also need to add some support to your .bashrc to ensure virtualenvwrapper works properly.
There's a tutorial here: http://virtualenvwrapper.readthedocs.org/en/latest/

##user
This repository ought to be located in a dedicated 'weeabot' user's home directory at:
/home/weeabot/code/weeabot_site
This can be created by the following commands:
```
useradd weeabot
su weeabot
cd ~
mkdir code
cd code
git clone https://github.com/on-three/weeabot_site.git
```
Using a dedicated user is recommended when running a web site via django.

##Nginx
I've configured this repository to work with the Nginx high performance web server. You could get it to work with anything else I think, but the weeabot.ngix.conf is especially configured for nginx only.
```
sudo apt-get instal nginx
```

##uwsgi
This repository also contains a uwsgi conf that ought to properly configure the web gateway between nginx and the django applicaiton.

#create virtualenv
it requires a dedicated project virtualenv (via virtualenvwrapper) at:
/home/weeeabot/.virtualenv/weeabot
This can be done as:
```
mkvirtualenv weeabot
```

#Python dependencies
Sign in as the weeabot user and activate your virtualenv and install the python dependencies via the included requirements.txt. Not that these wil be installed into your virtualenv, protecting your system from odd python versions and modules.
```
su weeabot
workon weeabot
cd ~/code/weeabot_site
pip install -r requirements.txt
```
Contents of virtualenv are described in weeabot/requirements.txt

##Upstart (daemon) Support
Starting and stopping the IRC bot and the django web service 
copy weeabot.uwsgi.ini and weeabot.uwsgi.override to /etc/init to support upstart daemon

softlink the nginx configuration via:
sudo ln -s /home/weeabot/code/weeabot_site/weeabot_nginx.conf /etc/nginx/sites-enabled/weeabot_nginx.conf

and then restart nginx
sudo /etc/init.d/nginx restart

You may have to remove the 'default' site enabled at /etc/nginx/sites-enabled/

