import pandas as pd 
import numpy

# os.getcwd()
sf = pd.read_csv("./dogNames2.csv")
# print(df.head())
# print(df.info())
# print(df.describe())
print(type(sf))
# dataframe中排序的方法
sf = sf.sort_values(by='Count_AnimalName',ascending=False)

# pandas 中取行或者列的注意点
# -方括号写数字，表示取行，对行进行操作
# -方括号写字符串，表示的取列，对列进行操作
print(sf[:20])
print('*'*100)
print(sf['Row_Labels'])
print('*'*100)
print(sf[:20]['Row_Labels'])
print('*'*100)
print(sf[(sf['Count_AnimalName']> 800) & (sf['Count_AnimalName']< 1000) ])
print('*'*100)
print(sf[(sf['Row_Labels'].str.len()>4) & (sf['Count_AnimalName']>700)])