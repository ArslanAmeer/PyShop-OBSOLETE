from django.shortcuts import render
from django.http import HttpResponse


# our first view function

def index(request):
    return HttpResponse('Hello World')
