from tensorflow import keras
import tensorflow as tf
import numpy as np


model = keras.models.load_model('tensorflow_model_ultima_speranta.h5')

def get_prediction(path):
    classes =['batteries', 'clothes', 'e-waste', 'glass', 'light blubs', 'metal', 'organic', 'paper', 'plastic']


    img = tf.keras.preprocessing.image.load_img(path, target_size=(256, 256))
    img_array = tf.keras.preprocessing.image.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)

    predictions = model.predict(img_array)

    index1 = np.argmax(predictions)
    #print('index = ',index1)
    return classes[index1]

path = '6.jpeg'
print(get_prediction(path))