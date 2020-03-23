from django.shortcuts import render, redirect
from django.http import HttpResponse
import platform
from django.core.files.storage import FileSystemStorage


# Create your views here.


def index(request):

    return render(request,"base/home.html")

def gamef1(request):
    return render(request, 'gamef1/home.html')

def habitants(request):
    return render(request,'habitants/home.html')