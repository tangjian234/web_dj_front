

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

