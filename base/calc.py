from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
from keras import Sequential
from keras.models import model_from_json
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Dense, Flatten, Dropout, Activation
from keras.constraints import maxnorm
from keras.optimizers import SGD, Adam
import random
import os
import numpy as np
from keras.utils import np_utils


# datagen = ImageDataGenerator(
#         rotation_range=40,
#         width_shift_range=0.2,
#         height_shift_range=0.2,
#         rescale=1./255,
#         shear_range=0.2,
#         zoom_range=0.2,
#         horizontal_flip=True,
#         fill_mode='nearest')

main_folder = 'f1cars'
folders = os.listdir(main_folder)
img_size = 128




# for folder in folders:
#     i = 0
#     for batch in datagen.flow_from_directory(main_folder, target_size=(img_size, img_size), color_mode='rgb', classes=[folder],class_mode='categorical', batch_size=32, shuffle=True, seed=None, save_to_dir=f'{main_folder}\{folder}', save_prefix=f'{folder}_created', save_format='png', follow_links=False, subset=None, interpolation='nearest'):
#         i += 1
#         if i > 40:
#             break

# imgs = []
# for folder in folders:
#     print(f'Estou acessando a pasta {folder}')
#     images = os.listdir(f'{main_folder}\{folder}')
#
#     for image in images:
#         img = load_img(f'{main_folder}\{folder}\{image}',target_size=(img_size,img_size))
#         img_formated = img_to_array(img)
#         img_formated = img_formated.reshape((img_size,img_size,3))
#         imgs.append((img_formated,folder))
#
#
# X = []
# y = []
#
# random.shuffle(imgs)
# for features, target in imgs:
#     X.append(features)
#
#     y.append(folders.index(target))
#
# #Transform lists into arrays
# X = np.array(X)
# y = np.array(y)
#
# # Normalizing data
# X = X.astype('float32')/255
# y = np_utils.to_categorical(y)
# print(X.shape)
# print(y.shape)
#
# model = Sequential()
# model.add(Conv2D(64,(3,3),activation='relu', input_shape=(img_size,img_size,3),padding='same',kernel_constraint=maxnorm(3)))
# model.add(MaxPooling2D(pool_size=(2,2)))
#
# model.add(Conv2D(64, (3, 3), activation='relu', padding='same', kernel_constraint=maxnorm(3)))
# model.add(MaxPooling2D(pool_size=(2, 2)))
#
# model.add(Conv2D(64, (3, 3), activation='relu', padding='same', kernel_constraint=maxnorm(3)))
# model.add(MaxPooling2D(pool_size=(2, 2)))
#
# model.add(Flatten())
# model.add(Dense(64,activation='relu'))
# model.add(Dropout(0.3))
# model.add(Dense(len(folders), activation='softmax'))
# optimizer = SGD(momentum=0.9)
# model.compile(loss='categorical_crossentropy',optimizer=optimizer,metrics=['accuracy'])
# #
# print(model.summary())
# #
# model.fit(X, y, epochs=50, batch_size=32, validation_split=0.15)
#
# scores = model.evaluate(X,y,verbose=0)
# print("Accuracy: %.2f%%" % (scores[1]*100))
# #
# model_json = model.to_json()
# with open('model_f1car_keras.json','w') as json_file:
#     json_file.write(model_json)
# model.save_weights('model_f1car_keras.h5')




#load json and create model
json_file = open('../media/model_f1car_keras.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
#load weights into new model
loaded_model.load_weights("model_f1car_keras.h5")
print("Loaded model from disk")

try:
    final_image = load_img('TestBenneton2.jpg', target_size=(img_size,img_size))
    final_img_formated = img_to_array(final_image)
    final_img_formated = final_img_formated.reshape((img_size, img_size, 3))
    list = []
    list.append(final_img_formated)
    X_test = np.array(list)
    X_test = X_test.astype('float32')
    X_test = X_test/255
except:
    print("Photo wasn't found")



prediction = loaded_model.predict(X_test)

result = np.where(prediction[0] == np.amax(prediction[0]))
print(prediction*100)

for folder in folders:

    scuderia = folders.index(folder)
    if scuderia == result[0]:
        print(f'This car is a {folder}!')
