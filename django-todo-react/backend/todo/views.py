from django.shortcuts import render

# Create your views here.
# todo/views.py

from django.shortcuts import render

from rest_framework import viewsets          # add this
from .serializers import TodoSerializer,Amazon_Price_Tracker_Serializer,  Temp_Serializer    # add this
from .models import Todo,Amazon_Price_Tracker,Temp                     # add this

'''
The viewsets base class provides the implementation for CRUD operations by default,
what we had to do was specify the serializer class and the query set.
'''
class TodoView(viewsets.ModelViewSet):       # add this
  serializer_class = TodoSerializer          # add this
  queryset = Todo.objects.all()              # add this

class Amazon_Price_Tracker_View(viewsets.ModelViewSet):       # add this
  serializer_class = Amazon_Price_Tracker_Serializer          # add this
  queryset = Amazon_Price_Tracker.objects.all()              # add this

class Temp_View(viewsets.ModelViewSet):       # add this
  serializer_class = Temp_Serializer          # add this
  queryset = Temp.objects.all()              # add this