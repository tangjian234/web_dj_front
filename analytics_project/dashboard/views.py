from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.shortcuts import render
from dashboard.models import Order
from django.core import serializers



def dashboard_with_pivot(request):

    """
    1. Function : render a 
    Once called, this function will render dashboard_with_pivot.html - a template we'll define soon. It will contain the pivot table and pivot charts components.

    2. Request argument : 
    Its request argument, an instance of HttpRequestObject, contains information about the request, e.g., the used HTTP method (GET or POST). 

    3. What to render dashboard_with_pivot.html: The method render searches for HTML templates in a templates directory located inside the app’s directory.

    """
    return render(request, 'dashboard_with_pivot.html', {})


def pivot_data(request):
    """
    1. Function : 
    create an auxiliary method that sends the response with data to the pivot table on the app's front-end
    return : the data for rendering 
    """
    dataset = Order.objects.all()
    data = serializers.serialize('json', dataset)
    return JsonResponse(data, safe=False)    