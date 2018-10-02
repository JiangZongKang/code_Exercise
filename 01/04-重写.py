class Animal(object):
    def eat(self):
        print('-----吃------')

    def drink(self):
        print('-----喝------')

    def sleep(self):
        print('-----睡------')

    def play(self):
        print('-----玩------')


class Dog(Animal):  # 在这个地方继承父类
    def bark(self):
        print('-----汪汪叫----')

class Xiaotq(Dog):
    def fly(self):
        print('-----飞-------')
    def bark(self): # 此处就重写了bark方法，只调用自己的方法，不会再调用父类的方法了
        print('------狂叫-----')

xioatq = Xiaotq()
xioatq.fly()
xioatq.bark()
xioatq.sleep()
