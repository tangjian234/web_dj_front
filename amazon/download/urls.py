

#!/usr/bin/env python

#------------------------------------------------------------------------>
"""
{Description}

This module : map views.py function and href link  

{Classes} : 


{Methods} :  
 
  __author__ : Jian tang 

"""
#------------------------------------------------------------------------>
from django.urls import path
from .views import index, add_doc_info, input_asin, show_asin_detail, create_asin_task, show_asin_task, test_asin_task, background_view, person_view
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name='index'),  # empty : call the view.index
    path('create_asin_task', create_asin_task, name='create_asin_task'),
    path('show_asin_task', show_asin_task, name='show_asin_task'),
    
#<!-------------------------------------------------------------->    
 
    path('input_asin', input_asin, name='input_asin'),
    # show_asin data
    # empty : call the view.create
    path('add', add_doc_info, name='add_doc_info'),
    #path('add/', ModelCreateView.as_view(), name='person_add'),
    path('show_asin_detail', show_asin_detail, name='show_asin_detail'),
    path('test_asin_task', test_asin_task, name='test_asin_task'),

    path('test_asin_task/<first_name>', test_asin_task,
         name='test_asin_task_first_name'),

    #### direct call the function to display a simple result
    path('background_view', background_view, name='background_view'),
    path('person_view', person_view, name='person_view')

]
