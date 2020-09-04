from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from kineret.views import KineretHome, KineretRegister, KineretLogin,\
    KineretDashboard, logout_request, KineretPayment, KineretPaymentSuccess

app_name = "kineret"
urlpatterns = [
    path('', KineretHome.as_view(), name='home'),
    path('register/', KineretRegister.as_view(), name='register'),
    path('login/', KineretLogin.as_view(), name='login'),
    path('logout/', logout_request, name='logout'),
    path('dashboard/', KineretDashboard.as_view(), name='dashboard'),
    path('payment/', KineretPayment.as_view(), name='payment'),
    path('payment/success/', KineretPaymentSuccess.as_view(), name='payment-success'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
