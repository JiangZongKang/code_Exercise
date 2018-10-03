from sklearn.tree import DecisionTreeClassifier,export_graphviz
from sklearn.feature_extraction import DictVectorizer
from sklearn.model_selection import train_test_split,GridSearchCV
from sklearn.ensemble import RandomForestClassifier
import pandas as pd 

 
def dt():
    '''
    决策树对泰坦尼克号进行预测生死
    :renturn None
    '''
    # 读取数据
    data = pd.read_csv('http://biostat.mc.vanderbilt.edu/wiki/pub/Main/DataSets/titanic.txt')
    print(data.shape)

    
    # 处理数据，找出特征值和目标值
    x = data[['pclass','age','sex']]
    y = data['survived']
    # print(x)

    # 对缺失值进行处理
    x['age'].fillna(x['age'].mean(),inplace=True)
    x = pd.get_dummies(x,sparse=True)  
    #通过使用pandas中的get_dummies方法对有类别的数据处理成one-hot编码的形式

    # 分割数据到训练集和测试集
    x_train,x_test, y_train,y_test = train_test_split(x,y,test_size=0.25,random_state = 666)
    # print(x_train)

    # 进行处理(特征工程) 特征值是有类别的，需要进行0ne-hot编码处理
    # dict= DictVectorizer(sparse=False)
    # x_train = dict.fit_transform(x_train.to_dict(orient='records'))
    # x_test = dict.transform(x_test.to_dict(orient='records'))
    # print(dict.get_feature_names())
    print(x_train)

    # 使用决策树进行预测
    dst = DecisionTreeClassifier()
    dst.fit(x_train,y_train)
    # dst.predict_proba() 预测某个标签(目标值)的概率
    
    # print('预测的准确率为：',dst.score(x_test,y_test))

    # 导出决策树到本地
    # export_graphviz(dst,out_file='./tree.dot',feature_names=['age', 'pclass=1st', 'pclass=2nd', 'pclass=3rd', 'sex=female', 'sex=male'])

    # 随机森林进行预测 (超参数调优)
    rf = RandomForestClassifier(random_state=666)
    # rf.fit(x_train,y_train)
        # print('预测的准确率为：',rf.score(x_test,y_test))
    

    # 网格搜索与交叉验证 (就是进行调参)
    param = {'n_estimators':[80,120,200,300,500,800,1200],'max_depth':[5,8,15,25,30]}
    gc = GridSearchCV(rf,param_grid=param,cv=2)
    gc.fit(x_train,y_train)
    print('预测的准确率为：',gc.score(x_test,y_test))
    print('查看最好的参数模型:',gc.best_params_ )

    return None



if __name__ == '__main__':
    dt()