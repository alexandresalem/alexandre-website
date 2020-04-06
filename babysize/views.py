from django.shortcuts import render
from .forms import BabyForm
from .babysize import baby_chart
import pandas as pd
import matplotlib.pyplot as plt
# Create your views here.

def home(request):

    form = BabyForm()
    context = {}
    context['babyform'] = form

    return render(request, 'babysize/home.html',context)


def result(request):
    form = BabyForm(request.GET)
    form_data = {}
    if form.is_valid():
        for i in request.GET:
            form_data[i] = request.GET[i]

    # Retrieving data from Baby Chart function
    heightdata, weightdata, chart_title, days, w_y_label, h_y_label = baby_chart(form_data)

    form_data['P50_h'] = heightdata['P50'].tolist
    form_data['P5_h'] = heightdata['P5'].tolist
    form_data['P95_h'] = heightdata['P95'].tolist

    form_data['P50_w'] = weightdata['P50'].tolist
    form_data['P5_w'] = weightdata['P5'].tolist
    form_data['P95_w'] = weightdata['P95'].tolist

    form_data['Days'] = heightdata['Day'].tolist

    form_data['age'] = days
    form_data['chart_title'] = chart_title
    form_data['w_y_label'] = w_y_label
    form_data['h_y_label'] = h_y_label

    return render(request, 'babysize/result.html', form_data)


def test(request):


    return render(request, 'babysize/test.html')