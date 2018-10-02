class Dog(object):
    def print_self(self):
        print('hahahahah')


class Xiaotq(Dog):
    def print_self(self):
        print('hhhhhhhhhh')


def introduce(temp):
    temp.print_self()


dog1 = Dog()
dog2 = Xiaotq()
introduce(dog1)
introduce(dog2)

# 面向对象的3个要素： 封装、 继承、 多态
#  Python既支持面向对象 也支持面向过程