

import datetime
from django.dispatch import receiver, Signal
from django.core.signals import request_finished
from django.db.models.signals import post_save
import time
from django.contrib import messages
from django import forms
from django.shortcuts import render, HttpResponse
import logging
import sys
import os

from .models import Lead
from .models import ASIN, ASIN_Instance, ASIN_task, Task_Status,ASIN_Search_task,STATUS_CHOICES,NUMBER_CHOICES
from background_task import background
#from .tasks import person_view
from .models import Person

import django.dispatch
from bootstrap_datepicker_plus import DatePickerInput



from .asin_json_process import load_asin_json,create_task_result_json
from .apscheduler_handle import scrapy_scheduler

####### create logger
from log_lib import Logger
logger = Logger()

 
####### create scrapy scheduler object 
scheduler = scrapy_scheduler()
import datetime
# <!------------------------------------------------------------------------->

""" // MARK :  ASIN_Search_task_form """
class ASIN_Search_task_form(forms.ModelForm):
    '''
    <A class used to 

    <Attributes> 
    ----------
    scheduler : TwistedScheduler
    process : CrawlerProcess
    job_complete_status : 
      dictionary for each task_id : task complete is true, not complete is false, 
    task_id :pk of task 

    <Methods>
    -------
    __init__(self) :
      Initialize scheduler,  
    job_completed(self,event):    
      Call back function after scrapping task is completed
    '''

    def __init__(self, *args, **kwargs): 
      super(ASIN_Search_task_form, self).__init__(*args, **kwargs)
      start= datetime.date.today()
      end = start + datetime.timedelta(days = 1)
      self.fields['ASIN_Search_List'].initial  = 'Bluetooth Headset'
      self.fields['Number_Of_Result'].initial  = 20
      self.fields['Start_Time'].initial  = start
      self.fields['End_Time'].initial  = end
      self.fields['Request_Status'].initial  = 'Ready'
    
    # specify the name of model to use
    class Meta:
        model = ASIN_Search_task
        fields = "__all__"
        widgets = { 
          'ASIN_Search_List': forms.TextInput(attrs={'placeholder':'Bluetooth Headset'}),
          'Number_Of_Result': forms.Select(choices=NUMBER_CHOICES),
          'Start_Time': DatePickerInput(),
          'End_Time': DatePickerInput(),
        }

# forms/widgets
# https://docs.djangoproject.com/en/3.1/ref/forms/widgets/#django.forms.Textarea 
""" // MARK :  ASIN_task_form """
class ASIN_task_form(forms.ModelForm):
    
    def __init__(self, *args, **kwargs): 
      super(ASIN_task_form, self).__init__(*args, **kwargs)
      start= datetime.date.today()
      end = start + datetime.timedelta(days = 1)
      self.fields['ASIN_Name_List'].initial  = 'B08DDZZRJF'
      self.fields['Request_Description'].initial  = 'Download list of ASIN Periodicly, ASIN serperated by ;  '
      self.fields['Start_Time'].initial  = start
      self.fields['End_Time'].initial  = end
      self.fields['Request_Status'].initial  = 'Ready'
    
    # specify the name of model to use
    class Meta:
        model = ASIN_task
        fields = "__all__"
        widgets = { 
          'ASIN_Name_List': forms.TextInput(attrs={'placeholder':'ASINAS'}),
          'Request_Status': forms.Select(choices=STATUS_CHOICES),
          'Start_Time': DatePickerInput(),
          'End_Time': DatePickerInput(),
        }

        # hide a form fields


        # widgets = {'Request_Status': forms.HiddenInput()}

# <!--------------------------------------------------->
"""// MARK : Create_asin_task """
def create_asin_task(request):
    """
    Function :  
      1. 
      2. 

    Parameters :
      : request: Standard request, 
      : 
    """

    context = {}
    head_title = 'Create ASIN Task'
    # Create the  init value form according
    #start= datetime.date.today()
    #end = start + datetime.timedelta(days = 1) 
    """
    init_form ={
      'ASIN_Name_List':'A1',
      'Request_Description':'B1',
      'Start_Time':start,
      'End_Time':end,
      'Request_Status':'Ready',    
    }

    init_search_form ={
      'ASIN_Search_List':'Bluetooth',
      'Number_Of_Result':10,
      'Start_Time':start,
      'End_Time':end,
      'Request_Status':'Ready',    
    }
    """
    
    
    
    form = ASIN_task_form()
    search_form = ASIN_Search_task_form()
    if request.POST: 
       # get name 
        if 'asin-form' in request.POST:
          form = ASIN_task_form(request.POST, request.FILES)
        # form.fields['Request_Status'].widget.attrs['readonly'] = True
          # check if form data is valid
          if form.is_valid():
              logger.worker.warning('Saved')
              messages.success(request, 'Your task was updated successfully!')
              # save the form data to model
              form.save()
          else:    
              print("not valide")
        if 'search-form' in request.POST:
           print('searched')
           form = ASIN_Search_task_form(request.POST, request.FILES)
           if form.is_valid():
              logger.worker.warning.warning('Search Saved')
              messages.success(request, 'Your task was updated successfully!')
              # save the form data to model
              form.save()
           else:    
              print("search save not valide")
  
    context = {
          'head_title': head_title,
          'form': form,
          'search_form': search_form,
      }
    
    return render(request, 'create_asin_task.html', context=context)

import string_lib

"""// MARK : Show_asin_task """ 
def show_asin_task(request):      
    """
      1. Show the created asin download tasks (status); 
      2. Show the product 1 vs 1 key parameter comparision table 
      3. Plot different charts : line, radar

    Parameters :
      : request: Standard request, 
      : 
    """
    #  Get entries from ASIN_task database 
    all_objects = ASIN_task.objects.all()
 
    context = {'all_objects': all_objects}
    logger.worker.warning('log in show asin-0!')
    print('log - in show asin-0!')

    # Will run GET if reload, Get means reload 
    if request.method == 'GET':      
      #logger.worker.warning(request.GET)
      #logger.worker.warning(request.META['QUERY_STRING'])
      for task_id in scheduler.job_complete_status.keys(): 
        if (scheduler.job_complete_status[task_id]):
          # check scheduler task complete status : 
          task_entry = all_objects.get(pk=task_id)
          task_entry.Request_Status = "Complete"
          task_entry.save()
          logger.worker.warning(task_id + ": "+ task_entry.ASIN_Name_List + "  Status changed")
      
    # Will run POST if submite button is clicked inside form 
    if request.method == 'POST':
        logger.worker.warning(request.POST)
        if 'shutdown-id' in request.POST:
          logger.worker.warning('SHOUTdown')
          scheduler.handle_scrapy_stop()
        
        # delete a task 
        if 'delete-id' in request.POST:
        # see : show_asin_task.html 
        # delete_pk = request.POST.get("delete-id") = item.pk         
          delete_pk = request.POST.get("delete-id")
          all_objects.get(pk=delete_pk).delete()

        # run the task , add task to scheudlar: 
        if 'run-id' in request.POST:
            run_pk = request.POST.get("run-id")
            logger.worker.warning('run log request '+request.method)
            logger.worker.warning(run_pk)

            # Save the model item status change to ongoing
            t = all_objects.get(pk=run_pk)
            t.Request_Status = "Ongoing"
            t.save()
            # Launch background function
            entry=all_objects.get(pk=run_pk)
            asin_list=entry.ASIN_Name_List
            scrapy_data={}

            scrapy_data['asin_list'] =asin_list
            scrapy_data['task_id'] =run_pk
            #scrapy_data['start_time']=entry.Start_Time
            #scrapy_data['end_time']=entry.End_Time
            
            #scrapy_data=create_task_result_json(scrapy_data)


            # transfer asin list and task id into scheduler s
            scheduler.handle_scrapy_start(scrapy_data)
            logger.worker.warning('after run log request ')
        
        if 'plot-id' in request.POST:
          plot_pk = request.POST.get("plot-id")
          entry=all_objects.get(pk=plot_pk)
          asin_list=entry.ASIN_Name_List
          
          # Get asin_list and price data 
          context=load_asin_json(asin_list,context)
          print(context)
    return render(request, 'show_asin_task.html', context)
    
## <!--------------------------------------------------->
#### test datebase curb operation of a model database:
######## https://docs.djangoproject.com/en/3.1/topics/db/queries/
######## hhttps://docs.djangoproject.com/en/3.1/ref/models/querysets/
##### View


def person_view(request):
    logger = logging.getLogger(__name__)
    logger.worker.warning('st')

##### Delete
    for e in Person.objects.all():
        e.delete()

##### Create
    p1 = Person(name="Fred Flintstone")
    p2 = Person(name="John smith")
    p3 = Person(name="Leon Jackson")
    p1.save()
    p2.save()
    p3.save()

##### Display
    for e in Person.objects.all():
      logger.worker.warning(e.name)

##### Retrieving

###### 1. filter
    logger.worker.warning('filter')
    q = Person.objects.filter(name="John smith")
    for e in q.all():
      logger.worker.warning(e.name)

###### 2. get: one object
    logger.worker.warning('get')
    q = Person.objects.get(name="Leon Jackson")
    logger.worker.warning(q.name)

    ##### update
    logger.worker.warning('update')
    Person.objects.filter(name="Leon Jackson").update(
        name="Leon Jackson-changed")
    for e in Person.objects.all():
        logger.worker.warning(e.name)
    return HttpResponse("Hello")


#### <------
#### test for background _ view call background runing function hellow


#@background(schedule=5)
# delay for 5 seconds
@background(schedule=5)
def Background_runing_func():

    logger = logging.getLogger(__name__)
    logger.worker.warning('start run background')
    #
    ##### Place to insert background work

    #### trigger call back

    #p = Person(name="Fred Flintstone")
    #p.save()
    p = task_sender()
    p.send_task()

    print("triggered")


task_signal = django.dispatch.Signal()


class task_sender:
  def send_task(self):
    task_signal.send(self.__class__)


def background_view(request):
    Background_runing_func()
    logger = logging.getLogger(__name__)
    logger.worker.warning('gg')
    return HttpResponse("Hello")


## call back function : excute when the hello background function is called

#def save_profile(sender, instance, **kwargs):
#    print("Hello World Person saved!")


def call_back_func(sender, **kwargs):
    logger = logging.getLogger(__name__)
    logger.worker.warning("Hello World sender calling back func called  !")
# after receive


task_signal.connect(call_back_func, sender=task_sender)

#post_save.connect(save_profile, sender=Person)

####

#### <------


class LeadForm(forms.ModelForm):
    name = forms.CharField(max_length=250, required=True,
                           widget=forms.TextInput())
    clinic_name = forms.CharField(
        max_length=250, required=True, widget=forms.TextInput())
    phone = forms.CharField(max_length=8, required=True,
                            widget=forms.TextInput(attrs={'type': 'number'}))
    email = forms.CharField(
        max_length=250, required=False, widget=forms.TextInput())

    class Meta:
        model = Lead
        fields = ("clinic_name", "phone")

def add_doc_info(request):
    # d = getVariables(request,dictionary={'page_name': "Doctors",
    # 'meta_desc' : "Sign up "})
    d = {}
    if request.method == "POST":
        SalesForm = LeadForm(request.POST)

        if SalesForm.is_valid():
            name = SalesForm.cleaned_data['name']
            clinic_name = SalesForm.cleaned_data['clinic_name']
            phone = SalesForm.cleaned_data['phone']
            email = SalesForm.cleaned_data['email']

            # Saving to database
            lead = Lead(name=name, clinic_name=clinic_name,
                        phone=phone, email=email)
            lead.save()
    else:
        SalesForm = LeadForm()
    d['form'] = SalesForm
    return render(request, 'add_doc_info.html', context=d)

    # return render(request,  'add_doc_info.html', d, context_instance=RequestContext(request))

# Create your views here.

def index(request):
    head_title = 'Local Library Home Here'
    num_Request = ASIN.objects.all().count()

    context = {
        'head_title': head_title,
        'num_Request': num_Request,
    }
    return render(request, 'index.html', context=context)


# Create your views


 

def test_asin_task(request, first_name=""):

    # show current time , delay 10 s :

    some_list = ['m1', 'm2']

    string = 'all lower case become upper one'
    num = 3
    date = datetime.datetime.now()
    context = {'first_name': 'John',
               'last_name': 'Doe',
               'some_list': some_list,
               'num': num,
               'date': date,
               'string': string, }

# https://docs.djangoproject.com/en/3.1/intro/overview/#design-your-model
    print("inspect model ")
    r = Person.objects.all()
    print(r)
    print(Person.objects.get(name__startswith=first_name))

# Test_form 


    return render(request, 'test_asin_task.html', context)


# pass the pk_id parameter
model_task_signal = Signal(providing_args=["pk_id"])


class model_task_sender:
  def send_task(self):
    model_task_signal.send(self.__class__)


@background(schedule=5)
def scrappy_temp_func(run_pk):

    # represent scrappy task
    time.sleep(5)
    model_task_signal.send(sender=ASIN_task, pk_id=run_pk)

# Call back and update model item status to completed


@receiver(model_task_signal)
def scrappy_call_back_func(sender, **kwargs):
  #Get the parameter set :
    Dict = kwargs.items()
    for k, v in Dict:
      if k == "pk_id":
        run_pk = v
    print(run_pk)
    all_objects = ASIN_task.objects.all()
    t = all_objects.get(pk=run_pk)
    t.Request_Status = Task_Status.complete
    print(t.Request_Status)
    t.save()
    logger = logging.getLogger(__name__)
    logger.worker.warning("completed scrappy  !")



"""
Function :  

Parameters :
   : 
   : 
"""
def show_asin_detail(request):
    data = {}
    data = {}
    context = {
        'ID': data["ASIN"],
        'Title': data["title"],
        'Price': data["price"],
        'Bsr': data["bsr"],
    }
    logger = logging.getLogger(__name__)
    logger.worker.warning('log in show asin detail!')
    return render(request, 'show_asin_detail.html', context=context)


def start_scrape_asin(request):
    obj = ASIN.objects.get(id=1)
    obj.title = 'scrape_result_title'
    context = {
        'ID': obj.asin_id,
        'Title': obj.title,
        'Listing': obj.listing,
    }
    return render(request, 'show_asin_detail.html', context=context)


def input_asin(request):
    context = {}

    head_title = 'ASIN Form Input'
    # Create the form according
    asinform = ASINForm(request.POST or None, request.FILES or None)
    # check if form data is valid
    if asinform.is_valid():
        # save the form data to model
        asinform.save()

    context = {
        'head_title': head_title,
        'form': asinform,
    }
    return render(request, 'input_asin.html', context=context)


# Create Forms

##
# Input, display a model : ASIN
##

# 1. Create form view as input to ASIN data


class ASINForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = ASIN
        fields = "__all__"
        widgets = {
            'ASIN_Name_List': forms.Textarea(attrs={"rows": 3, "cols": 10}),
            'Request_Description': forms.Textarea(attrs={"rows": 3, "cols": 10}),
        }