class Base(object):
    def test(self):
        print('-----Base')
class A(Base):
    def test(self):
        print('-----A')
class B(Base):
    def test(self):
        print('-----B')
class C(A,B):
    def test(self):
        print('-----C')

c =C()
c.test()
print(C.__mro__) # 决定了调用一个方法的时候的搜索的顺序，
                 # 如果在某个类中找到了方法，那么就停止搜索
                 
