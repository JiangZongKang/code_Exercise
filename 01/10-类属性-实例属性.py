class Tool(object):
    num = 0  # 类属性
    
    # 实例方法
    def __init__(self, new_name):
        self.name = new_name  # 实例属性
        Tool.num += 1  # 对类属性+=1


tooll = Tool('铁锹')
tool2 = Tool('工兵铲')
tool3 = Tool('水桶')
print(Tool.num)
print('why to slow')


