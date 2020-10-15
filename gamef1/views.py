from django.urls import reverse
from django.views.generic import CreateView, UpdateView, TemplateView
from django.db.models import Avg
from .forms import *
from .tasks import predict, populate_model


class F1InputView(CreateView):
    model = F1Prediction
    fields = ['image']
    template_name = 'gamef1/home.html'

    def get_success_url(self):
        return reverse('gamef1:prediction',
                       kwargs={'pk': self.object.pk})


class F1PredictionView(UpdateView):
    model = F1Prediction
    form_class = F1PredictionResultForm
    template_name = 'gamef1/prediction.html'

    def form_valid(self, form, **kwargs):
        results = []
        for i in range(1, 11):
            results.append(f'sub_{i}')
        for result in results:
            if result in self.request.POST:
                prediction = self.get_context_data().get(f"place_{result.split('_')[1]}")
                form.instance.constructor = prediction[1]
                form.instance.chassis = prediction[0]
                form.instance.position = int(result.split('_')[1])
                form.instance.probability = prediction[3]
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(predict(self.object.image))
        return context

    def get_success_url(self):
        return reverse('gamef1:results')


class F1ResultsView(TemplateView):
    template_name = 'gamef1/results.html'

    def get_context_data(self, **kwargs):
        context = super(F1ResultsView, self).get_context_data()
        last_game = F1Prediction.cars.last()
        average = F1Prediction.cars.aggregate(Avg('position'))
        average = 100 + (average.get('position__avg') - 1) * -10
        context.update({
            'object': last_game,
            'average': average
        })
        return context
