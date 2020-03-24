from django.urls import path
from . import views

urlpatterns = [
    path('', views.habitants, name='habitants-home'),
    path('result', views.result, name='result')

]
