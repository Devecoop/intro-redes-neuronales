import tensorflow as tf

# Ruta del directorio que contiene las imágenes
directorio_imagenes = 'generated_images'

# Crear el dataset a partir del directorio de imágenes
dataset = tf.keras.preprocessing.image_dataset_from_directory(directorio_imagenes, 
                                                              image_size=(38, 38),
                                                              color_mode='grayscale',
                                                              label_mode='binary', 
                                                              labels='inferred')

tf.data.Dataset.save(dataset, 'rosenblatt_sample.tfrecord')
