import random

import pandas as pd
from django.core.files import storage
from django.core.files.storage import FileSystemStorage
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView, FormView

from gettingstarted.settings import STATIC_ROOT, STATIC_URL

static_storage = FileSystemStorage(location=STATIC_ROOT, base_url=STATIC_URL)
media_storage = FileSystemStorage()


class F1Pilot(TemplateView):
    template_name = 'f1pilot/home.html'


class F1PilotGame(TemplateView):
    template_name = 'f1pilot/game.html'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        file = static_storage.path(f'f1pilot/questions.csv')
        self.df = pd.read_csv(file)

        questions = list(self.df.columns[3:].values)
        answers = []
        for question in questions:
            answers.append(self.df[question].sum())
        self.question_round = questions[answers.index(max(answers))]

    def post(self, request, **kwargs):
        import ipdb; ipdb.set_trace()



        # if 'no' in request.POST:
        #     df = self.df[self.df[self.question_round] == 0].drop(columns=[self.question_round])
        # elif 'yes' in request.POST:
        #     df = self.df[self.df[self.question_round] == 1].drop(columns=[self.question_round])
        # elif 'dontknow' in request.POST:
        #     df = self.df.drop(columns=[self.question_round])

        # context = super().get_context_data(df=df)
        #
        # if len(df.index) == 1:
        #     driver = df['Answer'].values[0]
        #     context['question'] = f'The driver is {driver}'
        #     return render(request, self.template_name, context)
        # elif len(df.index) == 0:
        #     df = pd.read_csv(self.file)

        return render(request, self.template_name, {'df': 'test'})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        import ipdb; ipdb.set_trace()
        context['question_round'] = self.question_round

        return context
