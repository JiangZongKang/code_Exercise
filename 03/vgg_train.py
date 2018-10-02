from keras.applications.vgg16 import VGG16
from keras.layers import Input,Dropout,Dense,Flatten
from keras.models import Model
from keras.datasets import mnist
from keras.optimizers import SGD
# import cv2
import h5py
import numpy as np 

model_vgg = VGG16(include_top=False,weights='imagenet',input_shape=(48,48,3))
for layer in model_vgg.layers:
    layer.trainable = False
model = Flatten(name='flatten')(model_vgg.output)
model = Dense(4096,activation='relu',name='fc1')(model)
model = Dense(4096,activation='relu',name='fc2')(model)
model = Dropout(0.5)(model)
model = Dense(10,activation='softmax')(model)
model_vgg_mnist = Model(inputs=model_vgg.input,outputs=model,name='vgg16')

# 打印模型结构，包括所需要的参数
model_vgg_mnist.summary()