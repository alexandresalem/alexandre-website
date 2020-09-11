from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "gamef1"
urlpatterns = [
    path('', views.F1PredictionView.as_view(), name='home'),
    path('<int:pk>/result/', views.F1PredictionResultView.as_view(), name='result')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
