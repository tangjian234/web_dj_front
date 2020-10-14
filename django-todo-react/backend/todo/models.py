from django.db import models
from django.utils.translation import gettext as _
# Create your models here.
# add this

# The code snippet above describes three properties on the Todo model:
# Title
# Description
# Completed

class Todo(models.Model):
  title = models.CharField(max_length=120) #
  description = models.TextField()
  completed = models.BooleanField(default=False)

  def _str_(self):
    return self.title

#B01J6A6H74
class Amazon_Price_Tracker(models.Model):
  Asin = models.CharField(max_length=10) #
  Description = models.TextField()
  Start_time=models.DateField(default="") # starting date: default today.
  End_time=models.DateField(default="")   # end data : default date : default 30 days
  #selector= models.CharField(max_length=20) #
  F3 = models.TextField()
  A6 = models.TimeField(default="")

  def _str_(self):
    return self.Asin

# create in
class Temp(models.Model):
  F1 = models.CharField(max_length=20) #
  F2 = models.CharField(max_length=3,
                        choices=[('A','ablitity'),('B','baby')],
                        default='A')
  F3=models.TextField()

  # # selection list :
  FRESHMAN = 'FR'
  SOPHOMORE = 'SO'
  YEAR_IN_SCHOOL_CHOICES = [
        (FRESHMAN, _('Freshman')),
        (SOPHOMORE,_('Sophomore'))
  ]
  year_in_school = models.CharField(
        max_length=2,
        choices=YEAR_IN_SCHOOL_CHOICES,
        default=FRESHMAN,
  )
  Start_date=models.DateField(default="")
  End_date=models.DateField(default="")
  Start_time=models.DateTimeField(default="")
  End_time=models.DateTimeField(default="")
  A3 = models.DateTimeField(default="")
  A5 = models.TimeField(default="")
  A6 = models.TimeField(default="")




  def is_upperclass(self):
        return self.year_in_school in {self.JUNIOR, self.SENIOR}

  def _str_(self):
    return self.F1