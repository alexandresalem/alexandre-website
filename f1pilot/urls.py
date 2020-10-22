from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "f1pilot"
urlpatterns = [
    path('', views.F1Pilot.as_view(), name='home'),
    path('game/', views.F1PilotGame.as_view(), name='game'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
