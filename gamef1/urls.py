from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "gamef1"
urlpatterns = [
    path('', views.F1InputView.as_view(), name='home'),
    path('<int:pk>/prediction/', views.F1PredictionView.as_view(), name='prediction'),
    path('results/', views.F1ResultsView.as_view(), name='results')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
