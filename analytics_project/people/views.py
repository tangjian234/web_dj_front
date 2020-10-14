from django.shortcuts import render
from .models import Person
from django.views.generic import CreateView
# Create your views here.
class PersonCreateView(CreateView):
    model = Person
    fields = ('name', 'email', 'job_title', 'bio')