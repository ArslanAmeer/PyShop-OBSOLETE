from django.http import HttpResponse
from django.views.generic.base import TemplateView, View
from django.views.generic.list import ListView
from django.template.response import TemplateResponse
from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import render
from .models import Product


# our first view function
# /products -> index

def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})


# class ProductView(ListView):
#     template_name = 'index.html'
#     model = Product
#
#     # def get_context_data(self):
#     #     products = Product.objects.all()
#     #     return {'products': products}
#     #
#     # def post(self):


def new(request):
    return HttpResponse('Hello to new World')
