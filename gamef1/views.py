from django.shortcuts import render, redirect
from .forms import *
from django.core.files.storage import FileSystemStorage
import requests
import base64
import urllib.request as ulib
import cv2
import numpy as np
import os
from django.conf import settings

# Create your views here.


def home(request):
    context = {}
    if request.method == 'POST':
        form = FormulaForm(request.POST)
        if form.is_valid():
            form.save()

            url = request.POST['imagelink']

            context['url'] = url

            urlbase = base64.b64encode(requests.get(url).content)


            try:
                ulib.urlretrieve(url, os.path.join(settings.BASE_DIR, 'static/f1predict.jpg'))

            except:
                print("Didn't work")
            finally:
                image = cv2.imread(os.path.join(settings.BASE_DIR, 'static/f1predict.jpg'))
                image = cv2.resize(image, (50, 50))

                image_array = np.array(image)
                image_array = image_array.astype('float32') / 255
                image_array = np.resize(image_array, (7500,))
                list = []
                for i in image_array:
                    list.append(i)
                context['array'] = list
                context['folder'] = 'vamos/testar'
                # print(image_array * 255)

            context['urlbase'] = urlbase

    form = FormulaForm()



    return render(request, 'gamef1/home.html', context)

