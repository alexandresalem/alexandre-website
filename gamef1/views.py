from django.shortcuts import render, redirect
from .forms import *
from django.core.files.storage import FileSystemStorage
import requests
import base64
import urllib.request as ulib
import cv2
import numpy as np
from django.conf import settings
import os

# Create your views here.


def home(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['f1image']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        url = fs.url(name)

        context['url'] = url

        image = cv2.imread(os.path.join(settings.MEDIA_ROOT, uploaded_file.name))
        image = cv2.resize(image, (50, 50))

        image_array = np.array(image)
        image_array = image_array.astype('float32') / 255
        image_array = np.resize(image_array, (7500,))
        list = []
        for i in image_array:
            list.append(i)
        context['array'] = list



        # context['urlbase'] = urlbase


        #
        #     urlbase = base64.b64encode(requests.get(url).content)
        #
        #
        #     try:
        #         ulib.urlretrieve(url, 'f2predict.jpg')
        #
        #     except:
        #         print("Didn't work")
        #     finally:




    return render(request, 'gamef1/home.html', context)

