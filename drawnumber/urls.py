from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django. contrib.auth.decorators import login_required

app_name="drawnumber"
urlpatterns = [
    path('', views.home, name='home'),
    # path('result', views.result, name='drawnumber-result'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)