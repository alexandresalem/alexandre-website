from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.index, name='home'),
    path('drawnumber/', include('drawnumber.urls',namespace='drawnumber')),
    path('habitants/', include('habitants.urls',namespace='habitants')),
    path('gamef1/', include('gamef1.urls',namespace='gamef1')),
    path('babysize/', include('babysize.urls',namespace='babysize')),
    path('jpmorgan/', include('jpmorgan.urls',namespace='jpmorgan')),
    path('kineret/', include('kineret.urls',namespace='kineret')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
