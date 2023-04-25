from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def display(request):
    s=" <h1> Welcome To Django Bumpher Class for free  </h1>"
    return HttpResponse(s)
