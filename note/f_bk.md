





## Listen learnt 
  must use virtual environment to isolate the development 

## Key info 

### final home ip address 
73.254.182.128


### Django 
#### django run and kill 
py manage.py runserver
http://127.0.0.1:8000/

kill server 
pkill -f runserver

### Reference 
https://mikesmithers.wordpress.com/2017/02/21/configuring-django-with-apache-on-a-raspberry-pi/

#### python django lib 
/home/pi/dvds/dvdsenv/lib/python3.7/site-packages
/home/pi/dvds/dvdsenv/lib/python3.7/site-packages/django/http/request.py
~/dvds/dvdsenv/lib/python3.7/site-packages/django/http 


https://maker.pro/raspberry-pi/projects/raspberry-pi-web-server
 inet 192.168.1.10  netmask 255.255.255.0  broadcast 192.168.1.255
 
Destination: 192.168.1.0 
Gateway: 192.168.1.1 

### apache
#### Reinstall apache 
re - invoke 
sudo apt-get purge apache2 -y ; sudo apt-get install apache2 -y
sudo apt-get purge libapache2-mod-wsgi-py3 ; sudo apt-get install libapache2-mod-wsgi-py3 


#### Start and restart apache 
- start : 
sudo service apache2 start
- restart 
sudo service apache2 restart
- stop 
sudo /etc/init.d/apache2 stop
- check status ,
sudo systemctl status apache2.service


#### apache error log 
apache error log : /var/log/apache2/error.log


## Boiler plate templete setting 

### Setup the djingo 
- Activate virtual env 
virtualenv dvdsenv
source dvdsenv/bin/activate

- Intall django in virtual env 
cd ~/dvds; source dvdsenv/bin/activate; pip install django
in the virtual env : 

- Kick start basic django project : dvds 
cd ~/dvds;django-admin.py startproject dvds .

- Modify settings.py 
sudo chmod 777 ~/dvds/dvds/settings.py; code ~/dvds/dvds/settings.py
change
    
    1. add dvds in installed_apps 
                'dvds'
    2. add static root 
    import os
    STATIC_ROOT = os.path.join( BASE_DIR, "static/")

- Keep the virtual env active and migrate model 
cd ~/dvds; source dvdsenv/bin/activate;./manage.py makemigrations; ./manage.py migrate

- Create admin 
./manage.py createsuperuser; 

- Collect static 
./manage.py collectstatic

- Run server : 
./manage.py runserver 

- change host : 
code ~/dvds/dvds/settings.py
ALLOWED_HOSTS = ['jian','73.254.182.128']

Expected result : standard django UI in browser .  
http://127.0.0.1:8000/


### Setup the apache  

- Install(re) Apache and wsgi : 
sudo apt-get purge apache2 -y ; sudo apt-get install apache2 -y
sudo apt-get purge libapache2-mod-wsgi-py3 ; sudo apt-get install libapache2-mod-wsgi-py3 

wsgi : bridge between django and apache 

- edit the 
sudo chmod 777 /etc/apache2/sites-available/000-default.conf; code /etc/apache2/sites-available/000-default.conf
Add 
   Alias /static /home/pi/dvds/static
    <Directory /home/pi/dvds/static> 
        Require all granted
    </Directory>
  
    <Directory /home/pi/dvds/dvds>
        <Files wsgi.py>
            Require all granted
        </Files>
    </Directory>
  
    WSGIDaemonProcess dvds python-path=/home/pi/dvds python-home=/home/pi/dvds/dvdsenv
    WSGIProcessGroup dvds
    WSGIScriptAlias / /home/pi/dvds/dvds/wsgi.py  

-  make the db accessable 

chmod g+w ~/dvds/db.sqlite3; chmod g+w ~/dvds ; sudo chown :www-data db.sqlite3; sudo chown :www-data ~/dvds

### expose to outside 
  

- add listen port 
sudo chmod 777 /etc/apache2/ports.conf ; code /etc/apache2/ports.conf
add Listen 80 

https://www.codepuppet.com/2014/02/08/enabling-external-access-to-your-apache-web-server-on-windows-7/

listen 80 already in /etc/apache2/ports.conf
set the port forwarding : /etc/apache2/ports.conf : get the latest 

- set portward : 
  - 192.168.1.1 : WAN -> virtual portforward 
  80 

- Result 
    http://73.254.182.128/ : my active server. 

question : enable the nord

### Restart computer 
    - just restart : the rpi is OK . 


## use nordvpn ? 

## 

## get the music of liziqi's work 

## update using backend todos. 

### Setup virtual env  

virtualenv backend_env
source ~/web/django-todo-react/backend/backend_env/bin/activate 

### install djingo into virtual env 
curl -sS https://bootstrap.pypa.io/get-pip.py | sudo python3

pip install django
pip install djangorestframework django-cors-headers

### change host 
in ~/web/django-todo-react/backend/backend/settings.py 
ALLOWED_HOSTS = ['jian','73.254.182.128']


### run django and test

./manage.py runserver
http://127.0.0.1:8000/api/


https://www.digitalocean.com/community/tutorials/build-a-to-do-application-using-django-and-react


### modify the apach config to point to the django file 
code /etc/apache2/sites-available/000-default.conf
cp /etc/apache2/sites-available/000-default.conf  /etc/apache2/sites-available/000-default.conf_dvds

sudo chmod 777 /etc/apache2/sites-available/000-default.conf; code /etc/apache2/sites-available/000-default.conf


/home/pi/web/django-todo-react/backend

   Alias /static /home/pi/web/django-todo-react/backend/static
    <Directory /home/pi/web/django-todo-react/backend/static> 
        Require all granted
    </Directory>
  
    <Directory /home/pi/web/django-todo-react/backend/backend>
        <Files wsgi.py>
            Require all granted
        </Files>
    </Directory>
  
    WSGIDaemonProcess backend python-path=/home/pi/web/django-todo-react/backend python-home=/home/pi/web/django-todo-react/backend/
    WSGIProcessGroup backend
    WSGIScriptAlias / /home/pi/web/django-todo-react/backend/backend/wsgi.py  


    ##  
    http://73.254.182.128/api/

    issue : can not edit the raw form 
    http://73.254.182.128/admin/
    user login only edit todos 





npm run-script build; sudo cp -r build /var/www/frontend


sudo cp -r ~/web/django-todo-react/frontend/build/* /var/www/frontend

## reading 

https://medium.com/@data.leon/django-for-data-scientists-tutorial-1-how-to-serve-a-machine-learning-model-with-django-464483423fd2

## structure 

html or react frontend to input a form 
djingo to take form input and put into a database 
apache access.

http://73.254.182.128/api/amazon/#post-generic-content-form



## Cookie cutter 
orginial 
https://vsupalov.com/cookiecutter-django-quickstart/


cutter usage 
https://github.com/pydanny/cookiecutter-django#usage
### install Virtualenvwrapper for Virtualenv management 

in ~/.bashrc add : 
export PROJECT_HOME=$HOME/Devel
source ~/.local/bin/virtualenvwrapper.sh
export WORKON_HOME=$HOME/.virtualenvs
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
export VIRTUALENVWRAPPER_VIRTUALENV=/usr/local/bin/virtualenv
export VIRTUALENVWRAPPER_ENV_BIN_DIR=bin  # <== This line fixed it for me

activate workon cut_env
deactivate :
### install   cookiecutter
sudo apt-get install cookiecutter

### setup the cookiecutter
cookiecutter https://github.com/pydanny/cookiecutter-django

#### Install apps according to requirement 

pip install -r requirements/local.txt

export DATABASE_URL="sqlite:///db.sqlite"
export CELERY_BROKER_URL="amqp://localhost"
export USE_DOCKER="yes"

#### Install apps according to requirement 
python manage.py migrate
$ python manage.py createsuperuser
$ python manage.py runserver

form 
https://tutorial.djangogirls.org/en/django_models/

https://medium.com/saarthi-ai/deploying-a-machine-learning-model-using-django-part-1-6c7de05c8d7



## dashbroad 
https://www.freecodecamp.org/news/how-to-create-an-analytics-dashboard-in-django-app/
### Questions : 
    1. make shortcut for runserver. 
    2. virtual environment setup and link to outside 

### Install basic django 
#### Basic set directory 
$ django-admin startproject analytics_project
$ python manage.py runserver
http://127.0.0.1:8000/

#### kick off prject 
1. Create prject 
project name : dashboard
$ python manage.py startapp dashboard

2. settings.py : add dashboard into Installed_prject 


echo $VIRTUAL_ENV

### Make django visualable from outside 

#### find venv 
workon 
echo $VIRTUAL_ENV

#### install wsgi and 
pip install djangorestframework django-cors-headers
sudo apt-get install libapache2-mod-wsgi-py3 

##### create super user  
./manage.py createsuperuser; 

#### build  static 
    ./manage.py collectstatic

#### add to setting.py : 
import os
STATIC_ROOT = os.path.join( BASE_DIR, "static/")
ALLOWED_HOSTS = ['jian','73.254.182.128','127.0.0.1']

##### migrate 
 ./manage.py makemigrations; ./manage.py migrate


-  make the db accessable 
cd /home/pi/web/analytics_project
chmod g+w ./db.sqlite3; chmod g+w . ; sudo chown :www-data db.sqlite3; sudo chown :www-data .

- modify the  000-default.conf 

    Define PROJECT analytics_project
    Define BASE_DIR /home/pi/web/analytics_project
    Define BASE_DIR_WSGI ${BASE_DIR}/analytics_project
    Define BASE_VENV  /home/pi/.virtualenvs/cut_env

 $ cp 000-default_anal.conf 000-default.conf ; sudo service apache2 restart


#### modify apache 


### Create html : Templates
#### Reference 
    https://www.freecodecamp.org/news/how-to-create-an-analytics-dashboard-in-django-app/

#### html 
    dashbroad/templates

    code dashboard_with_pivot.html

  <div id="pivot-table-container" data-url="{% url 'pivot_data' %}"></div>
  <div id="pivot-chart-container"></div>

#### what 
    pivot_data  - > function defined in views.py
    pivot_data  - > linked in urls

### Django structure

1. project : 
    base_directory : 
    $django-admin startproject analytics_project

2. project/project : analytics_project
    contain : project wide settings : 
    settings.py urls.py ets 

3. app 
    app : dashbroad 
    $python manage.py startapp dashboard

### Views

see views.py : 

def dashboard_with_pivot(request):
def pivot_data(request):

### Url 
build up the url structure : 
1. base url  
    from django.urls import path,include
    urlpatterns = [

        path('dashboard/', include('dashboard.urls')),
    ]
    connect dashboard.urls'
http://73.254.182.128/dashboard

2. 
map url to function : 
 - map '' to dashboard_with_pivot
 - map 'data' to pivot_data

    urlpatterns = [
        path('', views.dashboard_with_pivot, name='dashboard_with_pivot'),
        path('data', views.pivot_data, name='pivot_data'),
    ]
### Model  

1. Order is the data 
input method 
class Order(models.Model):
    product_category = models.CharField(max_length=20)
    payment_method = models.CharField(max_length=50)
    shipping_cost = models.CharField(max_length=50)
    unit_price = models.DecimalField(max_digits=5, decimal_places=2)

#### create model in database 
    Migration is simply a file that describes which changes must be applied to the database. Every time we need to create a database based on the model described by Python classes, we use migration.     

    1. create the migrate in dashbroad app
        $ python manage.py makemigrations dashboard; 
    2. create the model into database 
        $ python manage.py migrate dashboard

#### create one instance in 
use django shell <Q: hwo to run not as shell >
$ python manage.py shell

from dashboard.models import Order    
>>>o1 = Order(product_category='Books',payment_method='Credit Card',shipping_cost=39,unit_price=59)
>>> o1.save()

#### restart apache to reflect change in urls 
cp 000-default_anal.conf 000-default.conf ; sudo service apache2 restart


## django-crispy-forms 


### Reference 

https://simpleisbetterthancomplex.com/tutorial/2018/08/13/how-to-use-bootstrap-4-forms-with-django.html


https://github.com/sibtc/bootstrap-forms-example/blob/master/simpleproject/urls.py


### Installation
pip install django-crispy-forms

### Model 
    class Person(models.Model):
        name = models.CharField(max_length=130)
        email = models.EmailField(blank=True)
        job_title = models.CharField(max_length=30, blank=True)
        bio = models.TextField(blank=True)

### views 


