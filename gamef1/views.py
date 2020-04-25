from django.shortcuts import render, redirect
from .forms import *
from django.core.files.storage import FileSystemStorage
import requests
import base64
import urllib.request as ulib
import cv2
import numpy as np
from django.core.files.storage import default_storage
from django.core.files import File
import os
# Create your views here.


def home(request):
    context = {}
    if request.method == 'POST':
        form = FormulaForm(request.POST)
        if form.is_valid():
            url = request.POST['imagelink']
            context['url'] = url
            urlbase = base64.b64encode(requests.get(url).content)

            try:
                result = ulib.urlretrieve(url)
                Formula.imagephoto.save(os.path.basename(url),File(result[0]))
                Formula.save()
                form.save()
            except:
                return render(request, 'gamef1/home.html')
            finally:

                image = cv2.imread('f2predict.jpg')
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

