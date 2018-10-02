from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression,Ridge
from sklearn.linear_model import SGDRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.externals import joblib



def lg():
    '''
    线性回归去预测房价
    :return None
    '''
    #获取数据
    data = load_boston()
    # print(data.data)
    # print(data.target)

    #分割数据集到训练集和测试集
    x_train,x_test,y_train,y_test = train_test_split(data.data,data.target,test_size=0.25)
    print(x_train.shape)

    #进行标准化处理(特征值和目标值都是需要标准化处理的)，实例化两个标准化API
    std_x = StandardScaler()
    std_y = StandardScaler()

    x_train = std_x.fit_transform(x_train)
    x_test = std_x.transform(x_test)

    y_train = std_y.fit_transform(y_train.reshape(-1,1))
    y_test = std_y.transform(y_test.reshape(-1,1))

    #estimator 预测
    #正规方程求解方式预测
    liner = LinearRegression()
    liner.fit(x_train,y_train)
    print(liner.coef_)  #这里是打印权重W，对于每一个特征对应于一个权重
    y_predict_l = std_y.inverse_transform(liner.predict(x_test))
    print('正规方程预测的房价为：',y_predict_l)
    print('正规方程的均方误差为：',mean_squared_error(std_y.inverse_transform(y_test),y_predict_l))
    print('*'*150)

    #使用梯度下降来预测房价
    sgd = SGDRegressor()
    sgd.fit(x_train,y_train)
    print(sgd.coef_)
    y_predict = std_y.inverse_transform(sgd.predict(x_test))
    print('梯度下降预测的房子价格为：',y_predict)
    print('梯度下降的均方误差为：',mean_squared_error(std_y.inverse_transform(y_test),y_predict))
    

     #使用岭回归来预测房价
    rd = Ridge()
    rd.fit(x_train,y_train)
    print(rd.coef_)
    y_predict_r = std_y.inverse_transform(rd.predict(x_test))
    print('岭回归预测的房子价格为：',y_predict_r)
    print('岭回归的均方误差为：',mean_squared_error(std_y.inverse_transform(y_test),y_predict_r))


    

    return None

if __name__ == '__main__':
    lg()
