from django.urls import path
from . import views

urlpatterns = [
    # path('', views.ProductView.as_view()),
    path('', views.index),
    path('new/', views.new)
]
