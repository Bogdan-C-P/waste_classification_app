import tensorflow as tf
import numpy as np

model = None
output_class = ["Batteries", "Clothes", "E-waste", "Glass", "Light Blubs", "Metal", "Organic", "Paper", "Plastic"]
data = {
"Batteries":
	'how to recycle batteries: ',
"Clothes":
	'how to recycle clothes: ',
"E-waste":
	'how to recycle e-waste: ',
"Glass":
	'how to recycle glass: ',
"Light Blubs":
	'how to recycle light bulbs: ',
"Metal":
	'how to recycle metal: ',
"Organic":
	'how to recycle organic: ',
"Paper":
	'how to recycle paper: ',
"Plastic":
	'how to recycle plastic:  ',
}


def load_artifacts():
    global model
    model = tf.keras.models.load_model("model.h5")

def classify_waste(path):
    classes =['Batteries', 'Clothes', 'E-waste', 'Glass', 'Light Blubs', 'Metal', 'Organic', 'Paper', 'Plastic']


    img = tf.keras.preprocessing.image.load_img(path, target_size=(256, 256))
    img_array = tf.keras.preprocessing.image.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)

    predictions = model.predict(img_array)

    index1 = np.argmax(predictions)

    #print('index = ',index1)
    return classes[index1], data[classes[index1]]