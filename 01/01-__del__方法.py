class Dog(object):
    def __del__(self):
        print('------hhhh-----')


dog1 = Dog()
dog2 = dog1

del dog1  #不会调用__del__方法，因为这个对象有其他变量指向它，即 引用计算不是0
del dog2  #此时不会调用__del__方法，因为没有变量指向它了
print('================')
# 如果在程序结束时，有些对象还存在，那么Python解释器会自动调用它们的__del__方法来完成清理工作