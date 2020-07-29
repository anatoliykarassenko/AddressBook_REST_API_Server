"""
Definition of views.
"""

#from datetime import datetime
#from django.http import HttpRequest
from django.shortcuts import render 
from rest_framework.response import Response
from rest_framework import status 
from . import serializers 

def home(request):
    """renders the home page."""
    assert isinstance(request, httprequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'home page',
            'year':datetime.now().year,
        }
    )



def about(request):
    """renders the about page."""
    assert isinstance(request, httprequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'about',
            'message':'your application description page.',
            'year':datetime.now().year,
        }
    )