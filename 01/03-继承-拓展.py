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

xioatq = Xiaotq()
xioatq.fly()
xioatq.bark()
xioatq.sleep()
