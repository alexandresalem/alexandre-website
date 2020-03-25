from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', views.index),
    path('drawnumber/', include('drawnumber.urls')),
    path('habitants/', include('habitants.urls')),
    # path('gamef1/', include('gamef1.urls')),
    # path('babysize/', include('babysize.urls')),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)