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
    path('f1_pilot/', include('f1pilot.urls',namespace='f1pilot')),
    path('babysize/', include('babysize.urls',namespace='babysize')),
    path('jpmorgan/', include('jpmorgan.urls',namespace='jpmorgan')),
    path('kineret/', include('kineret.urls',namespace='kineret')),
    path('mensalidade/', include('mensalidade.urls',namespace='mensalidade')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = [
    url(r'^profile_update/$', views.profile_update, name="profile_update"),
    url(r'^profile_update/$', views.profile_update, name="profile_update"),
    url(r'^(?P<slug>[-\w]+)/update/$', views.EventProfileUpdateView.as_view(), name='event_profile_update'),
    url(r'^(?P<slug>[-\w]+)/update/$', views.EventProfileUpdateView.as_view(), name='event_profile_update'),
]
urlpatterns = [
    url(r'^(?P<slug>[-\w]+)/update/$', views.EventProfileUpdateView.as_view(), name='event_profile_update'),
    url(r'^profile_update/$', views.profile_update, name="profile_update"),
]