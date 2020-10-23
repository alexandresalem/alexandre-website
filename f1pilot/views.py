import pandas as pd
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from django.views.generic import TemplateView, FormView

from f1pilot.utils import get_question
from gettingstarted.settings import STATIC_ROOT, STATIC_URL

static_storage = FileSystemStorage(location=STATIC_ROOT, base_url=STATIC_URL)
media_storage = FileSystemStorage()


def f1pilot(request):

    if request.method == "POST":
        return render(request, 'f1pilot/game.html')

        # if 'start' in request.POST:
        #     sheet = static_storage.path('f1pilot/questions.csv')
        #     df = pd.read_csv(sheet)
        #     with open(sheet) as file:
        #         media_storage.save('f1pilot/questions.csv', file)
        #     question_round, result = get_question(df)
        #     context = {
        #         'question_round': question_round
        #     }
        #     return render(request, 'f1pilot/game.html', context)
        #
        # elif 'answer' in request.POST:
        #     answer = request.POST['answer']
        #     file = media_storage.path('f1pilot/questions.csv')
        #     df = pd.read_csv(file)
        #
        #     if len(df) <= 1:
        #         if answer == 'Yes':
        #             question_round, result = "Congratulations!", True
        #
        #             return render(request, 'f1pilot/game.html', {'question_round': question_round})
        #         else:
        #             media_storage.delete('f1pilot/questions.csv')
        #             sheet = static_storage.path('f1pilot/questions.csv')
        #             df = pd.read_csv(sheet)
        #             with open(sheet) as file:
        #                 media_storage.save('f1pilot/questions.csv', file)
        #             question_round, result = get_question(df)
        #             return render(request, 'f1pilot/game.html', {'question_round': question_round})
        #     else:
        #         question_round, result = get_question(df)
        #
        #     if answer == 'No':
        #         df = df[df[question_round] == 0].drop(columns=[question_round])
        #     elif answer == 'Yes':
        #         df = df[df[question_round] == 1].drop(columns=[question_round])
        #     elif answer == "Don't Know":
        #         df = df.drop(columns=[question_round])
        #
        #     df.to_csv(media_storage.path('f1pilot/questions.csv'), index=False)
        #     question_round, result = get_question(df)
        #
        #     return render(request, 'f1pilot/game.html', {'question_round': question_round, 'result': result})
    # 
    # return render(request, 'f1pilot/home.html')
