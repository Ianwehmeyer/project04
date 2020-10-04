from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='trader-home-page'),
]