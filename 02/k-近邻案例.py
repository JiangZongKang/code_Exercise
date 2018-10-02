from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split,GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report




def knniris():
    '''
    knn鸢尾花分类
    :retuen None
    '''

    # 实例化类
    iris = load_iris()

    # 查看数据规模
    print(iris.data.shape)
    # 查看样本的特征值
    # print(iris.data)
    # 查看样本的目标值
    # print(iris.target)

    # 对iris数据集进行分割
    x_train, x_test, y_train, y_test = train_test_split(iris.data,iris.target,test_size=0.25)
    print(x_train)
    print('-'*50)
    print(y_train0)

    # 对iris数据集进行标准化
    std = StandardScaler()
    x_train = std.fit_transform(x_train)
    x_test = std.transform(x_test)


    # 开始进行knn算法流程
    knn = KNeighborsClassifier()

    # 构造一些参数的值进行搜索
    param = {'n_neighbors':[3,5,7,10]}

    # 进行网格搜索与交叉验证
    gc = GridSearchCV(knn,param_grid=param,cv=10)
    gc.fit(x_train,y_train)
    y_predict = gc.predict(x_test)
    # 预测准确率
    print('在测试集上的准确率为：',gc.score(x_test,y_test))
    print('在交叉验证中最好的结果：',gc.best_score_)
    print('在交叉验证中最好的参数模型：',gc.best_estimator_)
    print('每次交叉验证的准确率结果：',gc.cv_results_)


    # 分类模型的精确率和召回率
    print('每个类别的精确率和召回率：',classification_report(y_test,y_predict,target_names=iris.target_names))

    
    # knn.fit(x_train,y_train)
    # y_predict = knn.predict(x_test)
    # score = knn.score(x_test,y_test)
    # print('预测的结果为:',y_predict)
    # print('准确率为：',score)

    # 查看数据说明
    # print(iris.DESCR)





    return None


if __name__ == '__main__':
    knniris()




