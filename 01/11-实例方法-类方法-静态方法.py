class Game(object):
    num = 0  # 类属性

    # 实例方法 ---> 通过实例方法去修改实例属性
    def __init__(self):  # 实例方法也必须要有参数
        self.name = 'laowang'  # 实例属性

    #  类方法 ——> 通过类方法去修改类属性，其类方法的定义比较特殊
    @classmethod
    def add_num(cls):  # 类方法必须要有参数
        cls.num = 100

    @staticmethod
    def print_meau():  # 静态方法可以不需要有参数
        print('---------------------')
        print('     穿越火线 V11.1   ')
        print('  1. 开始游戏   ')
        print('  2. 结束游戏   ')
        print('---------------------')


game = Game()
# Game.add_num() 可以通过类的名字调用类方法
game.add_num()   # 也可以通过这个类创建出来的对象，去调用这个类方法
print(Game.num)

# Game.print_meau()  通过类去调用静态方法
game.print_meau()  # 通过实例对象 去调用静态方法
