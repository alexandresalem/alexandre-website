from django.shortcuts import render, redirect
from .forms import *
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from .f1guesser import *
# Create your views here.


def home(request):

    return render(request, 'gamef1/home.html')

def result(request):
    if request.method == 'POST':
        image = request.FILES['car-photo']
        print(image.name)
        print(image.size)
        fs = FileSystemStorage()
        save = fs.save(image.name, image)
        url = fs.url(save)
        print(url)
        context = {}
        context['url'] = url



    return render(request, 'gamef1/result.html', context)

