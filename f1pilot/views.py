import pandas as pd
from django.core.files import storage
from django.core.files.storage import FileSystemStorage
# Create your views here.
from django.views.generic import TemplateView

from gettingstarted.settings import STATIC_ROOT, STATIC_URL

storage = FileSystemStorage(location=STATIC_ROOT, base_url=STATIC_URL)


class F1Pilot(TemplateView):
    template_name = 'f1pilot/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        file = storage.path('f1pilot/questions.csv')
        df = pd.read_csv(file)
        questions = list(df.columns[3:].values)
        answers = []
        for question in questions:
            answers.append(df[question].sum())

        first_question = questions[answers.index(max(answers))]
        context.update({
            'first_question': first_question
        })
        return context
