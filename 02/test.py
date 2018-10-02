from sklearn.feature_extraction import DictVectorizer
from sklearn.feature_selection import VarianceThreshold
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import PCA
from sklearn.preprocessing import MinMaxScaler,StandardScaler,Imputer
import numpy as np
import jieba
# vector = CountVectorizer()

# res = vector.fit_transform(['life is short ,i like python','life is too lang,i dislike python'])
# print(vector.get_feature_names())

# print(res.toarray())

def dictver():
    
    # 字典数据抽取
    
    # 实例化
    dict = DictVectorizer(sparse=False)

    # 调用fit_transform
    data = dict.fit_transform([{'city':'北京','temperature':100},
    {'city':'上海','temperature':60},
    {'city':'深圳','temperature':30}])
    print(dict.get_feature_names())
    # print(dict.inverse_transform(data)) 
    print(data)
    return None

def countvec():
    '''
    对文本进行特征值化
    '''
    cv = CountVectorizer()
    data = cv.fit_transform(['life is is short ,i like is python','life is too lang,i dislike python'])

    print(cv.get_feature_names())
    print(data.toarray())
    return None

def cutword():
    con1= jieba.cut('今天很残酷，明天更残酷，后天很美好，但绝大部分是死在明天晚上，所以每个人不要放弃今天')
    con2 = jieba.cut('我们看到的从很远星系来的光是在几百万年之前发出的，这样当我们看到宇宙时，我们是在看它的过去')
    con3 = jieba.cut('如果只用一种方式了解某样事物，你就不会真正了解它。了解事物真正含义的秘密取决于如何将其与我们所了解的事物相联系')
    #转换成列表
    content1 = list(con1)
    content2 = list(con2)
    content3 = list(con3)

    print(content3)
    return None
def hanzivec():
    '''
    中文特征值化
    '''
    cv = CountVectorizer()
    data = cv.fit_transform([])

    print(cv.get_feature_names())
    print(data.toarray())

    return None

def mm():  
    '''
    归一化处理
    '''
    mm = MinMaxScaler(feature_range=(2,3))
    data = mm.fit_transform([[90,2,10,40],[60,4,15,45],[75,3,13,46]])
    print(data)

def stand():
    '''
    标准化缩放
    '''
    std = StandardScaler()
    data = std.fit_transform([[1,-1,3],[2,4,2],[4,6,-1]])
    print(data)

def im():
    '''
    缺失值处理
    ''' 
    im = Imputer(axis=1)
    data = im.fit_transform([[1,2],[np.nan,3],[7,6]])
    print(data)

def var():
    '''
    特征选择-删除低方差的特征
    '''
    var = VarianceThreshold(threshold=1.0)
    data = var.fit_transform([[0,2,0,3],[0,1,4,3],[0,1,1,3]])
    print(data)
 
    return None

def pca():
    '''
    主成分分析
    '''
    pca = PCA(n_components=0.9)
    data = pca.fit_transform([[2,8,4,5],[6,3,0,8],[5,4,9,1]])
    print(data)

    return None

if __name__ == '__main__':
    pca()