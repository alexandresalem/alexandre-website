from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic import FormView
from django.views.generic.base import TemplateView
import stripe

from gettingstarted.settings import STRIPE_API_KEY
from kineret.forms import UserCreationForm, UserAuthenticationForm

stripe.api_key = STRIPE_API_KEY

class KineretHome(TemplateView):
    template_name = 'kineret/home.html'

    def get_context_data(self, **kwargs):
        super().get_context_data()
        context = {'user': None}
        return context


class KineretRegister(FormView):
    form_class = UserCreationForm
    template_name = 'kineret/register.html'

    def form_valid(self, form):

        return redirect('kineret:dashboard')


class KineretLogin(FormView):
    form_class = UserAuthenticationForm
    template_name = 'kineret/login.html'

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(self.request, user)
            return redirect('kineret:dashboard')


class KineretDashboard(LoginRequiredMixin, TemplateView):
    login_url = '/kineret/login/'
    template_name = 'kineret/dashboard.html'

    def get_context_data(self, **kwargs):
        user = self.request.user
        context = {'user': user}
        return context


class KineretPayment(LoginRequiredMixin, TemplateView):
    login_url = '/kineret/login/'
    template_name = 'kineret/payment.html'

    def get_context_data(self, **kwargs):
        user = self.request.user
        context = {'user': user}
        return context

    def form_valid(self, form):

        stripe.Customer.create(
            email=self.request.user.email,
            name=self.request.user.first_name,
            api_key='sk_test_51HMlyrFHy6lOMvj4NRbkApGcVzDeCrntahWCiDx0CyQ1IkgHThq1Uq1QYu8n36LevzNw3nCTCeyJCisgbiMUptts00S7mc8VNU')


class KineretPaymentSuccess(LoginRequiredMixin, TemplateView):
    login_url = '/kineret/login/'
    template_name = 'kineret/payment-success.html'

    def get_context_data(self, **kwargs):
        user = self.request.user
        context = {'user': user}
        return context


def logout_request(request):
    logout(request)
    return redirect("kineret:home")
