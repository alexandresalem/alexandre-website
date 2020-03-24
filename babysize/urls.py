from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='babysize-home'),
    path('result/', views.result, name='babysize-result'),
    path('test/', views.test, name='babysize-test'),

]
