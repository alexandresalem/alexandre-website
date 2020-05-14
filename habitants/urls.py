from django.urls import path
from . import views

app_name="habitants"
urlpatterns = [
    path('', views.habitants, name='home'),
    path('result', views.result, name='result')

]
