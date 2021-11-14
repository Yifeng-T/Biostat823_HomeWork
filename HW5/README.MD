Made By Yifeng Tang  
[GitHub](https://github.com/Yifeng-T/Biostat823_HomeWork/tree/main/HW5) Page

# HW5
## Background
The goal of this project is to train a deep learning model to classify beetles, cockroaches and dragonflies using these [Images Sets](https://people.duke.edu/~ccc14/insects.zip). The images are from [Here](https://www.insectimages.org/index.cfm). Also, in the end, I used [Shaply Explanations](https://github.com/slundberg/shap) to evaluate the prediction result. 

## Strategy
I used [Tensorflow](https://github.com/tensorflow/tensorflow), which is a powerful images classification tool. 
The procedure to finish this machine learning project is:
* 1. Overview and understand the data
* 2. Build an input pipepline
* 3. Create the model
* 4. Train the model
* 5. Test the model
* 6. Evaluate the model

## Environment
The following are the required packages for this project:
```python
import matplotlib.pyplot as plt
import numpy as np
import os
import PIL
import tensorflow as tf

from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential
import pathlib
import glob

import shap
```
The edition of the required packages are:   
matplotlib == 3.3.1.   
numpy == 1.19.1.    
tensorflow == 2.7.0.   

## Preparing the data:
Overview:  
There are total number of 1019 pictures for train data. In the 1019 pictures, there are 460 for beetles, 240 for cockroach, and 319 for dragonflies.  
There are total number of 180 pictures for test data.   
You could use the following code to achive this:
```python
#train overall: number of total tarin pictures
train = [f for f in glob.glob('insects/train/*/*.jpg')]
print(len(train))

#test overall: number of total test pictures:
test = [f for f in glob.glob('insects/test/' + "*/*.jpg")]
print(len(test))

#train for beetles: number of train
train_beetles = [f for f in glob.glob('insects/train/beetles/*.jpg')]
print(len(train_beetles))
#number of train cockroach
train_cock = [f for f in glob.glob('insects/train/cockroach/*.jpg')]
print(len(train_cock))
#number of train dragonflies
train_drag = [f for f in glob.glob('insects/train/dragonflies/*.jpg')]
print(len(train_drag))
```
Standardized the images:
Before using the training data to create the model, we need to standardize the pictures first:
```python
#standardized the picture
batch_size = 32
img_height = 180
img_width = 180

#training data set:
train_ds = tf.keras.utils.image_dataset_from_directory(
  'insects/train/',
  image_size=(img_height, img_width),
  batch_size=batch_size)

#stabdardized test data set:
test_ds = tf.keras.utils.image_dataset_from_directory(
  'insects/test/',
  image_size=(img_height, img_width),
  batch_size=batch_size)
  
# keeps the images in memory after they're loaded off disk during the first epoch. 
AUTOTUNE = tf.data.AUTOTUNE

train_ds = train_ds.cache().shuffle(1000).prefetch(buffer_size=AUTOTUNE)
test_ds = test_ds.cache().prefetch(buffer_size=AUTOTUNE)

# standardized the pictures
normalization_layer = layers.Rescaling(1./255)
normalized_ds = train_ds.map(lambda x, y: (normalization_layer(x), y))
image_batch, labels_batch = next(iter(normalized_ds))
first_image = image_batch[0]
```

