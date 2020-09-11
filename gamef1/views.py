from django.urls import reverse
from django.views.generic import CreateView, UpdateView

from .forms import *
from .tasks import predict


class F1PredictionView(CreateView):
    model = F1Prediction
    fields = ['image']
    template_name = 'gamef1/home.html'

    def get_success_url(self):
        return reverse('gamef1:result',
                       kwargs={'pk': self.object.pk})


class F1PredictionResultView(UpdateView):
    model = F1Prediction
    form_class = F1PredictionResultForm
    template_name = 'gamef1/result.html'

    def form_valid(self, form, **kwargs):
        for result in ['sub_first', 'sub_second', 'sub_third']:
            if result in self.request.POST:
                form.instance.constructor = self.get_context_data().get(result.split('_')[1])[0]
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        kwargs.update(predict(self.object.image))
        context = super().get_context_data(**kwargs)
        context.update(predict(self.object.image))
        return context

    def get_success_url(self):
        return reverse('gamef1:home')

