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
class Cat(Animal):
    def catch(self):
        print('-----抓老鼠----')


a = Animal()
a.eat()
wangcai = Dog()
wangcai.play()
wangcai.bark()
tom = Cat()
tom.play()
tom.catch()