import enum
import logging
import uuid
from django.db import models

from datetime import datetime,date
from django.db.models import signals
from datetime import timedelta

# E:\home\pi\pylib
# import string_lib
# import string

################


# The first element in each tuple is the actual value to be set on the model, and the second element is the human-readable name.
# Status of a ASIN_TASK; it is a string 
STATUS_CHOICES = [ 
    ("Ready", "Ready"), 
    ("Ongoing", "Ongoing"), 
    ("Complete", "Complete"), 
    ("Error", "Error"), 
 ]

# top No of search result :  e.g top 4 of the bluetooth headset search 
NUMBER_CHOICES = [ 
    (1, 1), 
    (2, 2), 
    (3, 3), 
    (4, 4), 
    (5, 5), 
    (6, 6), 
    (7, 7), 
    (8, 8), 
    (9, 9), 
    (10, 10),
 ]
class ASIN_task(models.Model):
  """
    <ASIN_task(models.Model): Main model for ASIN download task given a list of asin sperated by ;  
    ...

    <Attributes>
    ----------
    ASIN_task_uuid : pk of the model 
    ASIN_Name_List : list of asin sperated by ;
    Request_Description : <option> task description
    Start_Time : start time of download task
    End_Time :start time of download task
    Request_Status : is task ready to be run, completeor  ongoing  
    <Methods>
    -------
 
  """

  #  ASIN : request
  #asin_name = models.ForeignKey('ASIN', on_delete=models.SET_NULL, null=True) #
  # Task_ID= get_random_string(8)
  #ASIN_Request_ID =  models.TextField(default="")
  # ASIN_Request_ID =  models.TextField(Task_ID)
  #ASIN_task_id= get_random_string(3)
  ASIN_task_uuid = models.UUIDField(
      primary_key=True, default=uuid.uuid4, editable=False)

  ASIN_Name_List = models.CharField(max_length=63, default="a1-")
  Request_Description = models.CharField(max_length=63, default="b1-")
  Start_Time = models.DateTimeField(default=datetime.now)  # starting date: default today.
  # end data : default date : default 3
  Interval=models.DurationField(default=timedelta(seconds=5))
  End_Time = models.DateTimeField(default=datetime.now)
  Request_Status = models.CharField(max_length=63,choices=STATUS_CHOICES)
 
class ASIN_Search_task(models.Model):
  """
    <ASIN_Search_task(models.Model): Main model for ASIN download task given a search word string such as "bluetooth headset"  
    ...

    <Attributes>
    ----------
    ASIN_Search_task_uuid : pk of the model 
    ASIN_Search_List : search word string such as "bluetooth headset"  
    Start_Time : start time of download task
    End_Time :start time of download task
    Request_Status : is task ready to be run, completeor  ongoing  
    <Methods>
    -------
 
  """  
  ASIN_Search_task_uuid = models.UUIDField(
      primary_key=True, default=uuid.uuid4, editable=False)

  ASIN_Search_List = models.CharField(max_length=63, default="a1-")
  Number_Of_Result = models.IntegerField(default=10,choices=NUMBER_CHOICES)
  Start_Time = models.DateTimeField(default=datetime.now)  # starting date: default today.
  # end data : default date : default 3
  End_Time = models.DateTimeField(default=datetime.now)
  Request_Status = models.CharField(max_length=63,choices=STATUS_CHOICES) 
 
# test
# from datetime import date


# <!------------------------------------------------------------------------->
class Book(models.Model):
  book_id = models.CharField(max_length=20)


class Book2(models.Model):
  book_if = models.CharField(max_length=20)


class Lead(models.Model):
    name = models.CharField(max_length=1300)
    clinic_name = models.CharField(max_length=1300)
    phone = models.IntegerField()
    email = models.EmailField(blank=True)
    submitted_on = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return u"%s %s" % (self.clinic_name, self.phone)


################

# Create your models here.


class ASIN(models.Model):

  """
    ASIN : static content : 
  """
  # asin_id= models.CharField(max_length=20)
  # title= models.TextField(max_length=400)
  asin_id = 'default_asian_id'
  title = 'default_asian_title'
  #listing=models.TextField(max_length=1000)

###  background task


class Person(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name


def user_post_save(sender, signal, *args, **kwargs):
    logger = logging.getLogger(__name__)
    logger.warning('after save called back ')


signals.post_save.connect(user_post_save, sender=ASIN)
###

#


class ASIN_Instance(models.Model):
  """
  # ASIN_Instance : dynamic content : change everyday 
  """
  # default values
  asin = models.ForeignKey('ASIN', on_delete=models.SET_NULL, null=True)
  price = 0.0
  product_best_seller_rank = 0
  # todo : init as a download time in precise second of the day
  # todo : test hwoto get the time
  extract_time = 1

  # price = models.FloatField()
  # ranking= models.IntegerField()
  #  extract_date = models.DateField(default="")


####### creating enumerations using class
class Task_Status(enum.Enum):
    ready = 1
    ongoing = 2
    complete = 3
    error = 4
