from django.views.generic import TemplateView, FormView, ListView
from .forms import CompanyForm
from .models import Company
from django.db.models import Q

from .utils import bloomberg, price


class StocksView(FormView):
    template_name = 'stocks/home.html'
    form_class = CompanyForm


class StocksResultView(FormView):
    template_name = 'stocks/results.html'
    form_class = CompanyForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('name')
        company = Company.objects.get(Q(pk=query))

        stock_price = price(company.symbol)
        context.update({
            'company': company,
            'news': bloomberg(company),
            'stock_price': stock_price
        })

        return context
