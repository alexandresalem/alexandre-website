from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import base64
import re
import numpy as np
import cv2
import os

from django.conf import settings

# Create your views here.


def home(request):


    # # form = NumberForm()
    # # load weights into new model
    # loaded_model.load_weights(os.path.join(settings.MEDIA_ROOT,'model5.h5')
    # print("Loaded model from disk")

    # if request.method == 'POST':
    # image = request.POST['img']
    #
    # from io import BytesIO
    # from PIL import Image
    #
    # image_data = re.sub("^data:image/png;base64,", "", image)
    # image_data = base64.b64decode(image_data)
    # output = open('drawnumber/static/drawnumber/assets/output.png', 'wb')
    # output.write(image_data)
    # output.close()
    #
    # try:
    #     final_image = cv2.imread('drawnumber/static/drawnumber/assets/output.png')
    #
    #     final_image = cv2.resize(final_image, (28, 28))
    #     print('PHOTO OK')
    # except:
    #     print("Photo wasn't found")
    #
    # final_image = np.array([final_image])
    #
    # final_image = final_image.astype(float) / 255
    #
    # print('Photo prepared to be run in the model')


        #
        # results = loaded_model.predict(final_image)
        # print('Rodando modelo em cima da foto salva')
        # number = np.argmax(results)
        # print(number)
        # print('O valor previsto é este')


        # context = {}


    return render(request, 'drawnumber/home.html')

