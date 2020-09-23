import json

import cv2
import numpy as np
from django.core.files.storage import FileSystemStorage
from tensorflow.keras.models import model_from_json

from gamef1.models import Chassis
from gettingstarted.settings import STATIC_ROOT, STATIC_URL, GAMEF1_CONSTRUCTOR_MODEL

IMG_SIZE = 50
storage = FileSystemStorage(location=STATIC_ROOT, base_url=STATIC_URL)


def load_model(team=None):
    if not team:
        model = storage.path(f'{GAMEF1_CONSTRUCTOR_MODEL}.json')
    else:
        model = storage.path(f'{GAMEF1_CONSTRUCTOR_MODEL}-{team}.json')

    with open(model, 'r') as file:
        loaded_model_json = file.read()

    loaded_model = model_from_json(loaded_model_json)
    # load weights into new model
    if not team:
        loaded_model.load_weights(storage.path(f"{GAMEF1_CONSTRUCTOR_MODEL}.h5"))
    else:
        loaded_model.load_weights(storage.path(f"{GAMEF1_CONSTRUCTOR_MODEL}-{team}.h5"))

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

    results = load_json(storage.path(f'{GAMEF1_CONSTRUCTOR_MODEL}_constructor_results.json')).get('results', None)
    chassis_info = load_json(storage.path('gamef1/assets/chassis.json'))

    resp = {}

    count = 1
    extra = 0
    podium = 5
    # Taking the 4 most probable constructors
    for i in range(0, podium):
        constructor_position = np.where(prediction[0] == np.amax(ranking[i]))[0][0]

        # Taking the most probable cars inside each constructor
        chassis_prediction = load_model(team=results[constructor_position]).predict(final_image)
        ranking_chassis = sorted(chassis_prediction[0], reverse=True)

        car_qty = podium + extra - i
        if len(chassis_prediction[0]) < car_qty:
            extra = car_qty - len(chassis_prediction[0])
            new_len = len(chassis_prediction[0])
        else:
            new_len = 4+extra-i
            extra = 0

        for j in range(0, new_len):
            chassis_position = np.where(chassis_prediction[0] == np.amax(ranking_chassis[j]))[0][0]

            chassis_results = load_json(storage.path(
                f'{GAMEF1_CONSTRUCTOR_MODEL}-{results[constructor_position]}_chassis_results.json')).get(
                'results', None)

            car_name = chassis_info.get(chassis_results[chassis_position])[1]
            car_constructor = chassis_info.get(chassis_results[chassis_position])[2]
            car_season = f"({', '.join(chassis_info.get(chassis_results[chassis_position])[0])})"
            probability = round(ranking_chassis[j] * ranking[i] * 100, 2)

            resp.update({
                f'place_{count}': [car_name, car_constructor, car_season, probability]
            })

            count += 1

        if i == podium - 1 and extra > 0:
            podium += 1

        sort_result = sorted(resp.items(), key=lambda x: x[1][3], reverse=True)

    resp = {}
    for item in range(0, len(sort_result)):
        resp.update({
            f'place_{item + 1}': sort_result[item][1]
        })

    return resp


def load_json(file) -> dict:
    with open(file, 'r') as file:
        data = file.read()
    return json.loads(data)


def populate_model():
    data = load_json(storage.path('gamef1/assets/chassis.json'))
    for chassis, info in data.items():
        Chassis.objects.get_or_create(
            chassis=chassis,
            constructor=info[2],
            chassis_fullname=info[1]
        )
