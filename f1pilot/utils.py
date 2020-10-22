import pandas as pd
from django.core.files.storage import FileSystemStorage

from gettingstarted.settings import STATIC_URL, STATIC_ROOT

static_storage = FileSystemStorage(location=STATIC_ROOT, base_url=STATIC_URL)
media_storage = FileSystemStorage()


def get_question(df):
    result = False
    questions = list(df.columns[3:].values)
    answers = []
    for question in questions:
        answers.append(df[question].sum())

    question_round = questions[answers.index(max(answers))]

    if len(df.index) == 1:
        driver = df['Answer'].values[0]
        question_round = f'Is the driver {driver}?'
        result = True
    elif len(df.index) == 0:
        file = static_storage.path('f1pilot/questions.csv')
        df = pd.read_csv(file)
        df.to_csv(media_storage.path('f1pilot/questions.csv'), index=False)
        question_round = get_question(df)

    return question_round, result
