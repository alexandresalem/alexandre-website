import pandas as pd
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import FormView, TemplateView

from f1pilot.forms import F1PilotForm
from f1pilot.utils import get_question
from gettingstarted.settings import STATIC_ROOT, STATIC_URL

static_storage = FileSystemStorage(location=STATIC_ROOT, base_url=STATIC_URL)
media_storage = FileSystemStorage()


class F1PilotView(FormView):
    template_name = 'f1pilot/home.html'
    form_class = F1PilotForm

    def get_success_url(self):
        return reverse('f1pilot:game')


class F1PilotGameView(TemplateView):
    template_name = 'f1pilot/game.html'
