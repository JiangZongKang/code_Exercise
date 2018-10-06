'''
如何为元组中的每个元素命名（使用元组可以减小存储开销，但是使用索引访问时降低了程序的可读性）提高程序的可读性？
解决方案：
    定义类似与其他语言的枚举类型，定义数值变量
    使用collections.namedtuple 替代内置的tuple
'''
from collections import namedtuple

#  define int variables
name, age, sex, email = range(4)
student = ('JiangZongKang', 23, 'male', 'jzksuccess@gmail.com')
print(student[email])    
       
      
    
       
# use collections.namedtuple
Student = namedtuple('student_info', ['name', 'age', 'sex', 'email'])   # 相当于定义了一个Student类
s = Student('JiangZongKang', 23, 'male', 'jzksuccess@gmail.com')        # 这是实例化类
print(s.email)                                                          # 直接调用对象中的某个属性


