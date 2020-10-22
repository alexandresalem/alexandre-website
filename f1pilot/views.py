import pandas as pd
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from django.views.generic import TemplateView

from f1pilot.utils import get_question
from gettingstarted.settings import STATIC_ROOT, STATIC_URL

static_storage = FileSystemStorage(location=STATIC_ROOT, base_url=STATIC_URL)
media_storage = FileSystemStorage()


class F1Pilot(TemplateView):
    template_name = 'f1pilot/home.html'

    def post(self, request, **kwargs):
        if 'start' in self.request.POST:
            file = static_storage.path('f1pilot/questions.csv')
            df = pd.read_csv(file)
            df.to_csv(media_storage.path('f1pilot/questions.csv'), index=False)
            question_round, result = get_question(df)
            context = {
                'question_round': question_round
            }
            return render(request, 'f1pilot/game.html', context)

        elif 'answer' in self.request.POST:
            answer = self.request.POST['answer']
            file = media_storage.path('f1pilot/questions.csv')
            df = pd.read_csv(file)

            if len(df) <= 1:
                file = static_storage.path('f1pilot/questions.csv')
                df = pd.read_csv(file)
                df.to_csv(media_storage.path('f1pilot/questions.csv'), index=False)
                question_round, result = get_question(df)
                return render(request, 'f1pilot/game.html', {'question_round': question_round})
            else:
                question_round, result = get_question(df)

            if answer == 'No':
                df = df[df[question_round] == 0].drop(columns=[question_round])
            elif answer == 'Yes':
                df = df[df[question_round] == 1].drop(columns=[question_round])
            elif answer == "Don't Know":
                df = df.drop(columns=[question_round])

            df.to_csv(media_storage.path('f1pilot/questions.csv'), index=False)
            question_round, result = get_question(df)

            return render(request, 'f1pilot/game.html', {'question_round': question_round, 'result': result})
