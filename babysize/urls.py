from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name="babysize"
urlpatterns = [
    path('', views.home, name='home'),
    path('result/', views.result, name='result'),
    path('test/', views.test, name='test'),

]
