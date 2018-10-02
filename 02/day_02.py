from sklearn.datasets import load_iris,fetch_20newsgroups,load_boston
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd 
# li = load_iris()
# ld = load_digits()
# print('获取特征值')
# print(ld.data)
# print('获取目标值')
# print(ld.target)
# print(ld.DESCR)

# 注意返回值，训练集 train x_train, y_train  测试集 test  x_test, y_teat
# x_train,x_test ,y_train, y_test = train_test_split(li.data,li.target,test_size=0.25)

# print('训练集特征值和目标值：',x_train,y_train)
# print('测试集特征值和目标值：',x_test,y_test)


# news = fetch_20newsgroups(subset='all')
# print(news.data)
# print(news.target)

# lb = load_boston()
# print('获取特征值')
# print(lb.data.shape)

# print(lb.data)
# print('获取目标值')
# print(lb.target.shape)
# print(lb.target)
# print(lb.DESCR)


def knncls():
    '''
    k-近邻预测用户的签到位置
    '''
    #读取数据
    data = pd.read_csv('./train.csv')
    print(data.head(10))
    #处理数据

    #特征工程（标准化）

if __name__ == '__main__':
    knncls()