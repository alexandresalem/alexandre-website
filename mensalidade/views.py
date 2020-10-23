from django.shortcuts import render
from django.urls import reverse

from django.views.generic import CreateView, TemplateView


class MensalidadeView(TemplateView):
    # model = F1Prediction
    # fields = ['image']
    template_name = 'mensalidade/home.html'

    # def get_success_url(self):
    #     return reverse('mensalidade:home',
    #                    kwargs={'pk': self.object.pk})
