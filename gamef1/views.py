from django.shortcuts import render, redirect
from .forms import *
from django.core.files.storage import FileSystemStorage

# Create your views here.


def home(request):
    context = {}
    if request.method == 'POST':
        form = FormulaForm(request.POST)
        if form.is_valid():
            print('VALID')
            form.save()
            print(form)
        url = request.POST['imagelink']
        print(url)
        context['url'] = url

    form = FormulaForm()


    return render(request, 'gamef1/home.html', context)

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

