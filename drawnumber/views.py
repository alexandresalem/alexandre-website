from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import os
from .forms import NumberForm
from .models import Number

from django.conf import settings

# Create your views here.


def home(request):
    context = {}
    # if request.method == 'POST':
    #     form = NumberForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #
    #
    # form = NumberForm()
    #
    # context['form'] = form

    return render(request, 'drawnumber/home.html')

