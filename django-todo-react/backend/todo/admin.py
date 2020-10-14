from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Todo # add this
from .models import  Amazon_Price_Tracker # add this
from .models import  Temp # add this


class TodoAdmin(admin.ModelAdmin):  # add this
  list_display = ('title', 'description', 'completed') # add this

class Amazon_Price_Tracker_Admin(admin.ModelAdmin):  # add this
  list_display = ('Asin', 'Description','Start_time','End_time','F3','A6') # add this


class Temp_Admin(admin.ModelAdmin):  # add this
  list_display = ('F1', 'F2', 'F3','year_in_school','Start_date',
    'End_date','Start_time','End_time','A3','A5','A6') # add this  


# Register your models here.
admin.site.register(Todo, TodoAdmin) # add this

admin.site.register(Amazon_Price_Tracker, Amazon_Price_Tracker_Admin) # add this


admin.site.register(Temp, Temp_Admin) # add this
