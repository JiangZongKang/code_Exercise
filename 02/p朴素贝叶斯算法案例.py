from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB


def naviebayes():
    '''
    朴素贝叶斯进行文本分类
    :return None
    '''

    news = fetch_20newsgroups()
    print(news.data.shape)
    print(news.target.shape)







    return None

if __name__ == '__main__':
    naviebayes()