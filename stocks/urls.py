from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name="stocks"
urlpatterns = [
    path('', views.StocksView.as_view(), name='home'),
    path('results/', views.StocksResultView.as_view(), name='results'),
]
