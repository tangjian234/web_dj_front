# dj_note.md
- [dj_note.md](file:///C:/Local/Work/Python/PyLib/django-todo-react/backend/dj_note.md) 

  - [∞](#)


## Strategy 
  - Use simple django : to run backend web service first 
  - package the periodic Amazon Asin download 
  - upload django to a open website: heruko


## Todo 
  - [ ]   Understand [heruko](#understand-heruko) 
  - [x]   Sort the readings 
  - [ ]   package the periodic Amazon Asin download 

## Refernece 
  - [Build a To-Do application Using Django and React | DigitalOcean](https://www.digitalocean.com/community/tutorials/build-a-to-do-application-using-django-and-react)




# Content 

## Introduction
`Django REST framework (DRF).`
  #### Django REST framework
  - install djangorestframework
    
    Django REST framework is a powerful and flexible toolkit for building Web APIs


  ### React : `Frontend`
  - is a JS framework that is great for developing SPAs (single page applications) and it has solid documentation and a vibrant ecosystem around it.

  ### Django : `backend` 
    1. Definition  
      - is a Python web framework that simplifies common practices in web development. 
    2. Mature and stable 
      - Django has been around for a while, meaning most gotcha’s and problems have been solved, and there’s a set of stable libraries supporting common development needs.
  
  ### Structure 
  Key word : Django REST framework (DRF).
  
    1. For this application, React serves as the front-end or client side framework, handling UI and getting and setting data via requests to 
    
    2.  the Django back-end, which is an API built using the Django REST framework (DRF).
  
  ### Interaction 

    #### Django-cors-headers
    `connect between frontend and backend` 

    - A Django App that adds Cross-Origin Resource Sharing (CORS) headers to responses. 
    - This allows in-browser requests to your Django application from other origins.

    Django-cors-headers is a python library that will help in preventing the errors that we would normally get due to CORS.rules. In the CORS_ORIGIN_WHITELIST snippet, we whitelisted localhost:3000 because we want the frontend (which will be served on that port) of the application to interact with the AP. 

    #### what is cors : 
    - [Cross-origin resource sharing - Wikipedia](https://en.wikipedia.org/wiki/Cross-origin_resource_sharing)

    - Cross-origin resource sharing (CORS) is a mechanism that allows restricted resources on a web page to be requested from another domain outside the domain from which the first resource was served.[1]
    
      `allow request from frontend to be reponsed in the backend` 
    
    - A web page may freely embed cross-origin images, stylesheets, scripts, iframes, and videos.[2] Certain "cross-domain" requests, notably Ajax requests, are forbidden by default by the same-origin security policy. 
    
    - CORS defines a way in which a browser and server can interact to determine whether it is safe to allow the cross-origin request.[3] It allows for more freedom and functionality than purely same-origin requests, but is more secure than simply allowing all cross-origin requests


  #### Run the app 
  // ANCHOR IMPORTANT 

   1. run backend 
    - Run : python manage.py runserver
    - backend link: http://127.0.0.1:8000/api/todos/
   
   2. run frontend  
    - Run : yarn start 
    - Frontend connection : http://localhost:3000 

## Prerequisites 
  ### what
  1. Install necessary package 
  2. 
  
  ### Communication between PC and Raspberry pi
    #### ssh  
       - start Ubuntu in PC 
       - myip.sh : get the latest ip 
       - sudo ssh pi@192.168.1.ip

    #### File transfer 
       - Using filezilla : 
       - myip.sh : get the latest ip 
    
    #### vnc 
       - Registered in realvnc and cloud 

  ### Installers    
  
  - apt-get : 
    -  Linux system (both Ubuntu and debian) package install 
    -   works in rpi 
    -    
  - pip : 
    - Python package install 
  
  ### setup local python environnement
      - install pipenv
        - pip3 install pipenv
      - Setup virtual environment 
        - pipenv shell
    
    #### what 
      - pipenv : 
        - It automatically creates and manages a virtualenv for your projects
      - `shell` :
        - will spawn a shell with the virtualenv activated. This shell can be deactivated by using exit.
  
  ### Install and set up a local programming environment for Diango:
    -  pip3 install django 

  ### Install Node.js and Create a Local Development Environment

  - [Node.js and Raspberry Pi](https://www.w3schools.com/nodejs/nodejs_raspberrypi.asp)

    sudo apt-get update
    sudo apt-get dist-upgrade
    curl -sL https://deb.nodesource.com/setup_8.x | sudo -E bash -
    sudo apt-get install -y nodejs
    node -v

  ### Install  django rest framework 
    `pipenv install djangorestframework django-cors-headers`

  ### Install Frontend : npm and nodejs. the java module 
      $ sudo apt-get update
      $ sudo apt-get upgrade
      $ sudo apt-get install nodejs npm
      $ sudo chmod +rxw /usr/local/lib/ #  change the accessibility 
      $ npm install -g create-react-app
  
  ### install yarn : js package manager and runner 
      install yarn : nodes.js package installer 


## Djingo : Setting up the Backend 

### Result : 
  #### Scripts: to run and reset app 
  - djrun.sh 
  - djrun-reset.sh

  #### djrun : run after make changes to models 
  rpi: /usr/bin/mbin
    python manage.py makemigrations todo
    python manage.py migrate todo
    python3 /home/pi/web/django-todo-react/backend/manage.py runserver
  
  #### djrun-reset : reset model 
    `delete models and reset`
    rpi: /usr/bin/mbin
  
    rm /home/pi/web/django-todo-react/backend/todo/migrations/*
    rm ~/web/django-todo-react/backend/db.sqlite3
    python manage.py makemigrations
    python manage.py migrate

###  Init base application

  #### Build  Basic directory 
    
  - mkdir django-todo-react
    - cd django-todo-react

  ####  Set up virtual environment.
    - pip install pipenv
    - pipenv shell

  ####  Install django
    - pipenv install django
  
  #### Kick start the project: backnd   
    - django-admin startproject backend
    - cd backend
  
  #### build up basic app : todo 
    - python manage.py startapp todo
  
  #### apply model with todo 
    - python manage.py migrate
  
  #### Run application 
  
    - python manage.py runserver


### Add Admin 
  #### Register 
  Register your models here in admin.py

  python manage.py createsuperuse    


### Modify Setting.py:  
  
  ####  Add installed the application.
  - [settings.py](django-todo-react/backend/backend/settings.py)
  
  'corsheaders',            # add this
  'rest_framework',         # add this
  'todo'

  ####  Whitelist Front and port
  - [settings.py](django-todo-react/backend/backend/settings.py)
  
  #####  Modified from old : 
  CORS_ORIGIN_WHITELIST = (
        'localhost:3000/'
    )
  ##### To new 
  CORS_ORIGIN_WHITELIST = (
        'http://localhost:3000',
    )
###  Structure

  `Model - serializer - view - urls`
  
  1. Build model 
  2. Connect to serializer, so that is in database . 
  3. add to view 
  4. change urls.py so it is accessible
  5. migrate : run migrate to make it  

  - [models.py](django-todo-react/backend/todo/models.py)
  - [serializers.py](django-todo-react/backend/todo/serializers.py)
  - [views.py](django-todo-react/backend/todo/views.py)
  - [urls.py](django-todo-react/backend/todo/urls.py)


### Model 

#### Create mode :
  
  - [models.py](django-todo-react/backend/todo/models.py)
  
  ##### Example 1 
    input fields : 
        title = models.CharField(max_length=120)
        description = models.TextField()
        completed = models.BooleanField(default=False)

  ##### Example 2 
    class Temp(models.Model):
      F1 = models.CharField(max_length=20) # 
      F2 = models.TextField()
      F3=models.TextField()
      def _str_(self):
        return self.F1   

  ##### fields for models : Explanation 
    
    1. CharField 
      - .CharField(max_length=3,
                          choices=[('A','ablitity'),('B','baby')],
                          default='A')
      Selection list 
    2. TextField : 

    3. DateField : DateField(default="")
    4. TimeField : TimeField(default="")
  
  #####  _str_
  
    2. what is _str_ mean : class 
      This method returns the string representation of the object. 

      def __str__(self):
          return 'Person(name='+self.name+', age='+str(self.age)+ ')'
      print(p.__str__())
  ###### Reference

    - [Model field reference | Django documentation | Django](https://docs.djangoproject.com/en/3.1/ref/models/fields/)

    - [Django models: Declaring a list of available choices in the right way.](https://www.merixstudio.com/blog/django-models-declaring-list-available-choices-right-way/)

     - [DateTimeField - Django Models - GeeksforGeeks](https://www.geeksforgeeks.org/datetimefield-django-models/)

### Serizalizer
  `Add Serizalizer fields for a model class `
  #### Code 
  - [serializers.py](django-todo-react/backend/todo/serializers.py)

    from .models import Todo,Amazon_Price_Tracker, Temp
    class Temp_Serializer(serializers.ModelSerializer):
      class Meta:
        model = Temp
        fields = ('F1', 'F2', 'F3')    
    ##### Add fields in class
      class Temp(models.Model):
      F1 = models.CharField(max_length=20)
  
  #### Definition 
    - The serializers in REST framework work very similarly to Django's `Form` and `ModelForm` classes. 

    - Serializers allow complex data such as querysets and model instances to be converted to native Python datatypes that can then be easily rendered into JSON, XML or other content types. 

    - Serializers also provide deserialization, allowing parsed data to be converted back into complex types, after first validating the incoming data.

  ####  Reference
    - [Serializers - Django REST framework](https://www.django-rest-framework.org/api-guide/serializers/)


### View
  `Add view for a model class `
  - [views.py](django-todo-react/backend/todo/views.py)

  #### Code 
  views.py
  from .serializers import TodoSerializer,Amazon_Price_Tracker_Serializer,  Temp_Serializer    # add this
  from .models import Todo,Amazon_Price_Tracker,Temp  

  class Temp_View(viewsets.ModelViewSet):       # add this
      serializer_class = Temp_Serializer          # add this
      queryset = Temp.objects.all()              # add this
  
  #### Definition 

  ####  Reference


### Urls
  `add the model to urls `
  - [urls.py](django-todo-react/backend/todo/urls.py)
  
  #### Code 
    router.register(r'Temp', views.Temp_View, 'temp')     # add this
  
  #### Definition 
    add the model to urls 
  ####  Reference

### Propagating changes to models  
  
  #### djrun : run after make changes to models 
  
  rpi: /usr/bin/mbin
    python manage.py makemigrations todo
    python manage.py migrate todo
    python3 /home/pi/web/django-todo-react/backend/manage.py runserver
  
  ##### What     
    
  Migrations are Django’s way of `propagating changes you make to your models (adding a field, deleting a model, etc.)` into your database schema.
    
   - [Migrations | Django documentation | Django](https://docs.djangoproject.com/en/3.1/topics/migrations/)
  
    
## React : Setting up the frontend

###  Installation  
  
  #### install npm and nodejs. the java module 
  $ sudo apt-get update
  $ sudo apt-get upgrade
  $ sudo apt-get install nodejs npm

// ANCHOR now

  #### Install application : create-react-app
  - We will install the create-react-app CLI (command line interface) tool globally with this command:
   
    -  sudo chmod +rxw /usr/local/lib/ #  change the accessibility 
    -  npm install -g create-react-app

    ##### create-react-app 
    Since we are building our frontend using React, we want to use the create-react-app CLI tool because it registers optimal settings and several benefits such as Hot reloading and Service workers. 

  #### install yarn : nodes.js package installer 
      curl -o- -L https://yarnpkg.com/install.sh | bash

###  run frontend 

  $ create-react-app frontend
  $ cd frontend
  $ yarn start

  #### Front end run 
  `yarn start`
  
  will kick start the front end js : react : 

  Local:            http://localhost:3000
  On Your Network:  http://192.168.1.17:3000

###  Add 2 packages to work space : bootstrap reactstrap
  
  $ yarn add bootstrap reactstrap axios

  - yarn add : add js packages 
  
  - bootstrap : 
    - The most popular HTML, CSS, and JS library in the world.
    - Build responsive, mobile-first projects on the web with the world’s most popular front-end component library. Bootstrap is an open source toolkit for developing with HTML, CSS, and JS.
  
  - reactstrap: 
    - Stateless React Components for Bootstrap 4.

  -  axios
     -  make requests to the API endpoints on the backend server

### Modify front end : UI part 
  Build a form like table 

  - src/index.css
    - Bootstrap’s stylesheet 
  - src/index.js
    -  Bootstrap’s js code  
  - src/App.js : 
    -   
  use js to replace static html 

### Modify front end : Data part 
  - To handle actions such as adding and editing tasks, we will use a modal

  $ mkdir src/components
  
  - src/components/Modal.js

### Connection between frontend and backend
1.  Build the connection 
  /home/pi/web/django-todo-react/frontend/package.json
  Add : 
  "proxy": "http://localhost:8000", 


## Testing the application
  ### Run the app 
  1. run backend 
  python manage.py runserver
  http://localhost:8000/api  
  2. run frontend  
  yarn start :
  Frontend connection : 
  http://localhost:3000 

## Upload to website 

### Potential Choices 
  1. Google ：https://domains.google/ 
  2. Github. 
  3. Heroku 
 
### Use github page. 

 - tangjian234@gmail
 - Tangwin@123

### Understand heruko
  - [Deploying Python and Django Apps on Heroku | Heroku Dev Center](https://devcenter.heroku.com/articles/deploying-python)
  
  - [Deploy Your Django + React.js app to Heroku - DEV](https://dev.to/shakib609/deploy-your-django-react-js-app-to-heroku-2bck) 

  - [How to Deploy your App to Heroku from Raspberry Pi - DEV](https://dev.to/heroku/how-to-deploy-your-app-to-heroku-from-raspberry-pi-162k)

  #### what
  -  understand what is heruko and hwo does it work .
  -  example of support both rest front end and django backend . 
  -`Cloud apps` : 
    - [Deploy Your Django + React.js app to Heroku - DEV](https://dev.to/shakib609/deploy-your-django-react-js-app-to-heroku-2bck) 

  #### hwoto
    - support the 

  #### result
    <Question: What is heruko >
    <Answer: >
      - Heroku is a cloud platform as a service (PaaS) supporting several programming languages.
      - allow a developer to build, run and scale applications in a similar manner across most languages
    
    <Question: Is heruko free >
    <Answer: > 
    - Many developers are looking for a free cloud web hosting services to run their apps, blogs, or bots without the hassle of managing servers.
    Heroku provides, for free, a 5MB database

    - Heroku provides, for free, 1 dyno. A dyno is an instance of your application running and responding to requests. If each instance of your application can serve each request in 100ms, then you get 600 requests/minute with the free account.
 
    - Your application code and its assets (the slug) are limited to 300 MB in total. Your application also has access to the local filesystem, which can serve as an ephemeral scratch space for that specific dyno, and should be able to store at least 1 GB of data.

    <Question: How to use heruko to scrapy or need to run apache in local? >

    <Question: How does it compare with AWS>
    <Answer: Heroku is best suitable for Startups, Medium Businesses whereas AWS is mainly focused on Medium Businesses and Large Enterprises. Heroku can meet low computational demands whereas AWS can meet high/very high computational demands. Heroku doesn't needs infrastructure maintenance whereas AWS needs a dedicated DevOps guy. >




###  install heroku CLI 
  
  - sudo curl https://cli-assets.heroku.com/install.sh | bash

### run the program 
  npm install -g create-react-app
  create-react-app my-app
  cd my-app
  git init
  heroku create -b https://github.com/mars/create-react-app-buildpack.git
  git add .
  # git commit -m "react-create-app on Heroku"
  git commit --author="tangjian234 <tangjian234@gmail.com>" -m "Impersonation is evil."
  git push heroku master ## stop here .s
  heroku open

end result : the link : 
https://immense-crag-84666.herokuapp.com/

## run django on raspberry pi

- [Configuring Django with Apache on a Raspberry Pi | The Anti-Kyte](https://mikesmithers.wordpress.com/2017/02/21/configuring-django-with-apache-on-a-raspberry-pi/)

### enable virtualenv 
/home/pi/web/django-todo-react/backend

sudo pip3 install virtualenv
virtualenv backend_env
source backend_env/bin/activate


## Amazon download:  Background running 

### Package and run background daily scrappy in raspberry-pi

  #### what
  - 
  #### hwoto
  - 
  #### result

## Misc 

### curl 
- [10 Simple cURL Commands with Examples on Linux](https://www.fastwebhost.in/blog/what-is-curl-and-how-to-use-curl-commands-in-linux/)

###  To recover lost IP configuration 

  - sudo apt purge openresolv dhcpcd5   
  - sudo apt-get install dhcpcd5

#### Router 

 This IP address is the current router address.
 192.168.1.1

#### 
  Generated by NetworkManager
  nameserver 192.168.1.1

### DHCP configuration 
[20_min]
  DHCP stands for 揇ynamic Host Configuration Protocol?    The DHCP daemon is the process which assigns IP addresses to computers when they join a network, and gives them other important information about the network.

  sudo apt-get install dhcpcd5
  https://pimylifeup.com/raspberry-pi-static-ip-address/





  <!------------------------------------------------------------------------->

  

Here : 
## Steps  
https://www.digitalocean.com/community/tutorials/build-a-to-do-application-using-django-and-react

1. Create model in models.py file 

2. Create make migrate
    $ python manage.py makemigrations todo
3. Migrate. 
    $ python manage.py migrate todo
4. Register your models here.

### Create mode :
    input fields : 
      title = models.CharField(max_length=120)
      description = models.TextField()
      completed = models.BooleanField(default=False)

### Propagating changes to models 

#### Makemigrations
    $ python3 manage.py makemigrations todo

#### Migrations
    $ python3 manage.py migrate todo
    
    https://docs.djangoproject.com/en/3.1/topics/migrations/
    
    Migrations are Django’s way of propagating changes you make to your models (adding a field, deleting a model, etc.) into your database schema.

### Admin 
#### Register 
    Register your models here in admin.py

        python manage.py createsuperuse    


### Add todo iteams in  
    djrun.sh
    http://localhost:8000/admin/todo/todo/        

###  To recover lost IP configuration 

sudo apt purge openresolv dhcpcd5   
 sudo apt-get install dhcpcd5

### edit and work on the pi 
Using filezilla : 
default editor : 

