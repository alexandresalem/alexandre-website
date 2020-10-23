from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "f1pilot"
urlpatterns = [
    path('', views.F1PilotView.as_view(), name='home'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
