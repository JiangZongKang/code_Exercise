import numpy as np 
from keras.models import load_model
from keras.models import Sequential,Model
from keras.layers import Dense,Activation,Input
import matplotlib.pyplot as plt
import matplotlib.image as processimage

# ---------序列模型--------------
model = Sequential()
model.add(Dense(
    32,
    input_shape=(784,)
))
model.add(Activation('relu'))
model.add(Dense(10))
model.add(Activation('softmax'))
model.summary()

# ---------通用模型--------------
# 定义输入层
input = Input(shape=(784,))
# 定义各个连接层，假设从输入层开始，定义两个隐含层，都有64个神经元，都使用relu激活函数
x = Dense(64,activation='relu')(input)
x = Dense(64,activation='relu')(x)
# 定义输出层
y = Dense(10,activation='softmax')(x)

# 所有要素都齐备之后，就可以定义模型对象了，参数很简单，分别是输入和输出
model = Model(inputs=input,outputs=y)

# 进行编译
model.compile(optimizer='rmsprop',loss='categorical_crossentropy',metrics=['accuracy'])

# 进行训练
model.fit()
