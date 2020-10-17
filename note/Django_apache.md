
#  - [Django_apache.md](file:///C:/local/work/Web/web/note/Django_apache.md) 

## Todo 

  - [ ] 1. [Complete front end Crisp  form  study](#Form-django-crispy-forms-)
    
  - [ ] 2. [Cookie Cutter ](#Cookie-Cutter-)

  - [ ] 3. [Django dashboard](#analytics-dashboard-in-a-django-app)


## Lesson learnt 

  - must use virtual environment to isolate the development 

## Key info 

### Login  
  #### Raspberry pi login 
    pi@ 192.168.1.xx
    tangwin/
  #### 

### Find home ip address 
  - 73.254.182.128

### Virtualenv

  #### Mothod 1 ： Virtualenvwrapper 
  - [virtualenvwrapper 5.0.1.dev2 — virtualenvwrapper 5.0.1.dev2 documentation](https://virtualenvwrapper.readthedocs.io/en/latest/)
- [Setting up a Django development environment - Learn web development | MDN](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/development_environment)

    #####  1. Install :
      1. 
    ##### 2. Setting
    in ~/.bashrc add : 
      export PROJECT_HOME=$HOME/Devel
      source ~/.local/bin/virtualenvwrapper.sh
      export WORKON_HOME=$HOME/.virtualenvs
      export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
      export VIRTUALENVWRAPPER_VIRTUALENV=/usr/local/bin/virtualenv
      export VIRTUALENVWRAPPER_ENV_BIN_DIR=bin  # <== This line fixed it for me

    
    #####  3. Create  Environment
      mkvirtualenv env2

    #####  4. activate Environment
      workon cut_env

    #####  5. deactivate Environment
      deactivate :

    #####  6. list Environment
       echo $VIRTUAL_ENV
       ls $WORKON_HOME
       lssitepackages

  #### Mothod 2 ： Activate virtual env 
    virtualenv dvdsenv
    source dvdsenv/bin/activate


### Django : bare bone basic setup :
  #### bare bone basic setup :

    $ mkdir django_test; cd django_test;
    $ django-admin startproject mytestsite; cd mytestsite; 
    $ python3 manage.py runserver 
    $ 127.0.0.1:8000
  
### Django 

  #### Reference 
    - [Configuring Django with Apache on a Raspberry Pi | The Anti-Kyte](https://mikesmithers.wordpress.com/2017/02/21/configuring-django-with-apache-on-a-raspberry-pi/)


  #### Django run and kill 
    1. Run server 
      py manage.py runserver
      http://127.0.0.1:8000/

    2. Kill server 
      pkill -f runserver


  #### python django lib 
    /home/pi/dvds/dvdsenv/lib/python3.7/site-packages
    /home/pi/dvds/dvdsenv/lib/python3.7/site-packages/django/http/request.py
    ~/dvds/dvdsenv/lib/python3.7/site-packages/django/http 


    https://maker.pro/raspberry-pi/projects/raspberry-pi-web-server
    inet 192.168.1.10  netmask 255.255.255.0  broadcast 192.168.1.255
    
    Destination: 192.168.1.0 
    Gateway: 192.168.1.1 

### Apache

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


## Boiler plate Django 

### Setup the Django 

  1. Activate virtual env 
    virtualenv dvdsenv
    source dvdsenv/bin/activate

  2. Intall django in virtual env 
    cd ~/dvds; source dvdsenv/bin/activate; pip install django
    in the virtual env : 

  3. Kick start basic django project : dvds 
    cd ~/dvds;django-admin.py startproject dvds .

  4. Modify settings.py 
    sudo chmod 777 ~/dvds/dvds/settings.py; code ~/dvds/dvds/settings.py

  5. change
      
      1. add dvds in installed_apps 
                  'dvds'
      2. add static root 
      import os
      STATIC_ROOT = os.path.join( BASE_DIR, "static/")

  - Keep the virtual env active and migrate model 
    $ cd ~/dvds; source dvdsenv/bin/activate;./manage.py makemigrations; ./manage.py migrate

  - Create admin 
    $ ./manage.py createsuperuser; 

  - Collect static 
    $ ./manage.py collectstatic

  - Run server : 
    $ ./manage.py runserver 

  - change host : 
    $ code ~/dvds/dvds/settings.py

    ALLOWED_HOSTS = ['jian','73.254.182.128']

  Expected result : standard django UI in browser .  
  http://127.0.0.1:8000/


## Setup the apache  
// ANCHOR  <IMPORTANT >

### Setup   
  #### Install(re) Apache and wsgi : 
    $ sudo apt-get purge apache2 -y ; sudo apt-get install apache2 -y
    $ sudo apt-get purge libapache2-mod-wsgi-py3 ; sudo apt-get install libapache2-mod-wsgi-py3 

  `wsgi : bridge between django and apache` 

  #### edit the config file : 000-default.conf
    $ sudo chmod 777 /etc/apache2/sites-available/000-default.conf; code /etc/apache2/sites-available/000-default.conf

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

  ####  make the db accessable 

    chmod g+w ~/dvds/db.sqlite3; chmod g+w ~/dvds ; sudo chown :www-data db.sqlite3; sudo chown :www-data ~/dvds

### Expose to outside 

  #### Reference
    - [Enabling External Access to Your Apache Web Server on Windows 7 – Code Puppet](https://www.codepuppet.com/2014/02/08/enabling-external-access-to-your-apache-web-server-on-windows-7/)

  #### add listen port 
    $ sudo chmod 777 /etc/apache2/ports.conf ; code /etc/apache2/ports.conf
  add Listen 80 


  - listen 80 already in /etc/apache2/ports.conf

  set the port forwarding : /etc/apache2/ports.conf : get the latest 

  - set portward : 
    - 192.168.1.1 : WAN -> virtual portforward 
    80 

  - Result 
      http://73.254.182.128/ : my active server. 

  question : enable the nord

  #### Restart computer 
      - just restart : the rpi is OK . 

## Django: Todo : boiler palate 

### Base dir 
  /home/pi/web/analytics_project/templates

### Reference
  - [Build a To-Do application Using Django and React | DigitalOcean](https://www.digitalocean.com/community/tutorials/build-a-to-do-application-using-django-and-react)

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

## Django :  library tutorial

### Base dir 
  /home/pi/web/analytics_project/templates

### Reference 
  - [Django Web Framework (Python) - Learn web development | MDN](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django)

### basic setup 
  #### virtualenv 
    $ mkvirtualenv library_env
    $ workon library_env
  
  #### barebone basic setup :

    $ mkdir django_test; cd django_test;
    $ django-admin startproject mytestsite; cd mytestsite; 
    $ python3 manage.py runserver 
    $ 127.0.0.1:8000
  
  #### Topics : 
    - Use Django's tools to create a skeleton website and application.
    - Start and stop the development server.
    - Create models to represent your application's data.
    - Use the Django admin site to populate your site's data.
    - Create views to retrieve specific data in response to different requests, and templates to render the data as HTML to be displayed in the browser.
    - Create mappers to associate different URL patterns with specific views.
    - Add user authorization and sessions to control site behaviour and access.
    - Work with forms.
    - Write test code for your app.
    - Use Django's security effectively.
    - Deploy your application to production.

### Skeleton website 

  ####  Create project 

    folder_name =  
    project_name=locallibrary
    app_name=startapp
   
   - startproject
      mkdir django_projects ; cd django_projects
      django-admin startproject locallibrary; 

  #### Creating the application
   - startapp
    cd locallibrary; python3 manage.py startapp catalog
  
  #### Registering the catalog application

    ###### edit setting.py  
      add app name 
  
  #### urls  
    - The URL mappings are managed through the urlpatterns variable, which is a Python list of path() functions. 
  
    - Each path() function either associates a URL pattern to a specific view, which will be displayed when the pattern is matched, or with another list of URL pattern testing code (in this second case, the pattern becomes the "base URL" for patterns defined in the target module).
  
    - The urlpatterns list initially defines a single function that maps all URLs with the pattern admin/ to the module admin.site.urls , which contains the Administration application's own URL mapping definitions.
  
  

### 
## Form  django-crispy-forms 

    - [∞](#Form-django-crispy-forms-)

### Base dir 
  /home/pi/web/analytics_project/templates

### Reference 

  - [How to Use Bootstrap 4 Forms With Django](https://simpleisbetterthancomplex.com/tutorial/2018/08/13/how-to-use-bootstrap-4-forms-with-django.html)
  https://github.com/sibtc/bootstrap-forms-example/blob/master/simpleproject/urls.py
  - [bootstrap-forms-example/urls.py at master · sibtc/bootstrap-forms-example · GitHub](https://github.com/sibtc/bootstrap-forms-example/blob/master/simpleproject/urls.py)

### Installation
  pip install django-crispy-forms

### backend 

  #### Model 
      class Person(models.Model):
          name = models.CharField(max_length=130)
          email = models.EmailField(blank=True)
          job_title = models.CharField(max_length=30, blank=True)
          bio = models.TextField(blank=True)

  #### views 

  PersonCreateView : create a form 

  from django.views.generic import CreateView
  from .models import Person

  class PersonCreateView(CreateView):
      model = Person
      fields = ('name', 'email', 'job_title', 'bio')

  #### urls 
    from people.views import  PersonCreateView
    path('add/', PersonCreateView.as_view(), name='person_add'),
  
  #### form

### Frontend : Template : html 

#### base.html  
Framework of 

1. Use the hosted Bootstrap CDN:
   <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">
  
2.   container
    Format a content inside the container. 
    <div class="container">
      <div class="row justify-content-center">
        <div class="col-8">
          <h1 class="mt-2">Django People</h1>
          <hr class="mt-0 mb-4">
          {% block content %}
          {% endblock %}
        </div>
      </div>
    </div>


Todo: <make better container >

#### form.html 
with the view.py ; it wll look for 
view is the form-like 
Without any further change, Django will try to use a template named people/person_form.html

  {% extends 'base.html' %}

  {% load crispy_forms_tags %}

  {% block content %}
    <form method="post" novalidate>
      {% csrf_token %}
      {{ form|crispy }}
      <button type="submit" class="btn btn-success">Save person</button>
    </form>
  {% endblock %}

#### 

### 

sudo service apache2 restart


## Cookie Cutter 

### Base dir 
  ~/web/cut/cutter

###  Reference
  - Original 
    - [The Quickest Way to Create and Run a New Cookiecutter Django Project · vsupalov.com](https://vsupalov.com/cookiecutter-django-quickstart/)


  - cutter usage 
    - [GitHub - pydanny/cookiecutter-django: Cookiecutter Django is a framework for jumpstarting production-ready Django projects quickly.](https://github.com/pydanny/cookiecutter-django#usage)

### Install Virtualenvwrapper for Virtualenv management 

  ####  1. Install :
     1. 
  #### 2. Setting
   in ~/.bashrc add : 
    export PROJECT_HOME=$HOME/Devel
    source ~/.local/bin/virtualenvwrapper.sh
    export WORKON_HOME=$HOME/.virtualenvs
    export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
    export VIRTUALENVWRAPPER_VIRTUALENV=/usr/local/bin/virtualenv
    export VIRTUALENVWRAPPER_ENV_BIN_DIR=bin  # <== This line fixed it for me

  
  ####  3. Create  Environment
    mkvirtualenv env2

  ####  4. activate Environment
    workon cut_env

  ####  5. deactivate Environment
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



##  Analytics dashboard in a Django app

### Base dir 

  /home/pi/web/analytics_project/dashboard

### Objective 

   1. Study the sidebar structure. 
   2. 

### Reference
     - [How to create an analytics dashboard in a Django app](https://www.freecodecamp.org/news/how-to-create-an-analytics-dashboard-in-django-app/)

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


## Django with Machine Learning Model 

### Reference
  - [Django for Data Scientists | How to Serve A Machine Learning Model with Django | by Leon | Medium](https://medium.com/@data.leon/django-for-data-scientists-tutorial-1-how-to-serve-a-machine-learning-model-with-django-464483423fd2)


## use nordvpn ? 
