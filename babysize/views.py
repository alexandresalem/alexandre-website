from django.shortcuts import render
from django.views.generic import FormView, TemplateView

from .utils import baby_chart
from .forms import BabyForm


# Create your views here.
class BabyFormView(FormView):
    template_name = 'babysize/home.html'
    form_class = BabyForm
    success_url = '/result/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        return super().form_valid(form)


class BabyResultView(TemplateView):
    template_name = "babysize/result.html"

    def get_context_data(self, **kwargs):
        context = {k: v for k, v in self.request.GET.items()}
        heightdata, weightdata, chart_title, days, w_y_label, h_y_label = baby_chart(self.request.GET)
        context.update({
            'P50_h': heightdata['P50'].tolist,
            'P5_h': heightdata['P5'].tolist,
            'P95_h': heightdata['P95'].tolist,
            'P50_w': weightdata['P50'].tolist,
            'P5_w': weightdata['P5'].tolist,
            'P95_w': weightdata['P95'].tolist,
            'Days': heightdata['Day'].tolist,
            'age': days,
            'chart_title': chart_title,
            'w_y_label': w_y_label,
            'h_y_label': h_y_label,
        })

        return context
