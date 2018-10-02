import numpy as numpy
from keras.datasets import mnist
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers import Convolution2D, Activation, MaxPooling2D, Flatten, Dense,Dropout
from keras.optimizers import Adam

nb_class = 10
nb_epoch = 10
batchsize = 128

# 数据预处理
(x_train, y_train), (x_test, y_test) = mnist.load_data()
print(x_train.shape[0], x_test.shape[0])

# 设定数据的形状
x_train = x_train.reshape(-1, 28, 28, 1)
x_test = x_test.reshape(-1, 28, 28, 1)

# one-hot 编码
y_train = np_utils.to_categorical(y_train, nb_class)
y_test = np_utils.to_categorical(y_test, nb_class)

# 设置序列模型
model = Sequential()

# 1st conv2d layer
model.add(Convolution2D(
    filters=64,
    kernel_size=[3, 3],
    strides=1,
    padding='same',
    input_shape=(28, 28, 1)
))
model.add(Activation('relu'))
model.add(MaxPooling2D(
    pool_size=(2, 2),
    strides=2,
    padding='same',
))
# 设置dropout层，防止过拟合
model.add(Dropout(0.5))

# 2nd conv2d layer
model.add(Convolution2D(
    filters=128,
    kernel_size=[3, 3],
    strides=1,
    padding='same',
))
model.add(Activation('relu'))
model.add(MaxPooling2D(
    pool_size=(2, 2),
    strides=2,
    padding='same',
))
model.add(Dropout(0.5))

# 3nd conv2d layer
model.add(Convolution2D(
    filters=256,
    kernel_size=[3, 3],
    strides=1,
    padding='same',
))
model.add(Activation('relu'))
model.add(MaxPooling2D(
    pool_size=(2, 2),
    strides=2,
    padding='same',
))
model.add(Dropout(0.5))

# 把当前的层节点展平
model.add(Flatten())

# 1st full conneted dense
model.add(Dense(128))  # 有点不懂
model.add(Activation('relu'))

# 2sd full conneted dense
model.add(Dense(64))  # 有点不懂
model.add(Activation('relu'))

# 3st full conneted dense
model.add(Dense(32))  # 有点不懂
model.add(Activation('relu'))

# 4sd full conneted dense
model.add(Dense(10))
model.add(Activation('softmax'))

# 定义优化器和其他参数
# adam = Adam(lr=0.0001)

# 编译model
model.compile(
    optimizer='adagrad',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

# 训练神经网络
model.fit(
    x_train, y_train,
    epochs=nb_epoch,
    batch_size=batchsize,
    validation_data=(x_test, y_test)
)
evaluation = model.evaluate(x_test, y_test,verbose=1)
print(evaluation,'')

