from rest_framework import serializers
from .models import Todo,Amazon_Price_Tracker, Temp
# In the code snippet above, 
# we specified the model to work with and the fields we want to be converted to JSON.
class TodoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Todo
    fields = ('id', 'title', 'description', 'completed')


class Amazon_Price_Tracker_Serializer(serializers.ModelSerializer):
  class Meta:
    model = Amazon_Price_Tracker
    fields = ('Asin', 'Description','Start_time','End_time','F3','A6')    

class Temp_Serializer(serializers.ModelSerializer):
  class Meta:
    model = Temp
    fields = ('F1', 'F2', 'F3','year_in_school','Start_date',
    'End_date','Start_time','End_time','A3','A5','A6'
    )    

