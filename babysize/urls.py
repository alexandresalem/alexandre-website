from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name="babysize"
urlpatterns = [
    path('', views.BabyFormView.as_view(), name='home'),
    path('result/', views.BabyResultView.as_view(), name='result'),
]
