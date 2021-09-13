from django.shortcuts import render
from django.http import HttpResponse


# our first view function
# /products -> index

def index(request):
    return HttpResponse('Hello World')


def new(request):
    return HttpResponse('Hello to new World')
