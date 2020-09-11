import json

import cv2
import numpy as np
from django.core.files.storage import FileSystemStorage
from tensorflow.keras.models import model_from_json

from gettingstarted.settings import STATIC_ROOT, STATIC_URL, GAMEF1_CONSTRUCTOR_MODEL

IMG_SIZE = 50
storage = FileSystemStorage(location=STATIC_ROOT, base_url=STATIC_URL)

def load_model(team=None):
    # if not team:
    model = storage.path(f'{GAMEF1_CONSTRUCTOR_MODEL}.json')

    with open(model, 'r') as file:
        loaded_model_json = file.read()

    loaded_model = model_from_json(loaded_model_json)
    # load weights into new model
    loaded_model.load_weights(storage.path(f"{GAMEF1_CONSTRUCTOR_MODEL}.h5"))
    print("Loaded model from disk")

    return loaded_model


def predict(image):
    try:
        final_image = cv2.imread(image.path)
        final_image = cv2.resize(final_image, (IMG_SIZE, IMG_SIZE))
    except:
        print("Photo wasn't found")

    final_image = np.array([final_image])
    final_image = final_image.astype(float) / 255
    prediction = load_model().predict(final_image)
    ranking = sorted(prediction[0], reverse=True)
    first = np.where(prediction[0] == np.amax(ranking[0]))[0][0]
    second = np.where(prediction[0] == np.amax(ranking[1]))[0][0]
    third = np.where(prediction[0] == np.amax(ranking[2]))[0][0]

    results = load_json(storage.path(f'{GAMEF1_CONSTRUCTOR_MODEL}_result_dict.json')).get('results', None)

    return {
        'first': [results[first], round(ranking[0] * 100, 2)],
        'second': [results[second], round(ranking[1] * 100, 2)],
        'third': [results[third], round(ranking[2] * 100, 2)]
    }


def load_json(file) -> dict:
    with open(file, 'r') as file:
        data = file.read()
    return json.loads(data)
