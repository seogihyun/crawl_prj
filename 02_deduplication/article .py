import pymongo
import pandas as pd
#몽고db 기사.csv 불러오기
client = pymongo.MongoClient('mongodb:/[pw]/[ip]/')
db = client.news
collection = db.articles
items = collection.find()
df = pd.DataFrame(items)

#데이터 전처리
from datetime import date, timedelta

yesterday = date.today() - timedelta(1)
date = yesterday.strftime('%Y.%m.%d')
# date값과 같은(어제날짜) 기사만 df만들기
df = df[df['p_date'] == date ]
# remaval 날짜로 중복된 제거된 기사와 그렇지 않은 기사 구분
df['removal'] = date # 중복제거 된 기사 날짜로 표시

# 결측치 제거
df = df.drop(df.loc[df['content']==''].index) # 기사들중 문자열이 없이 이미지만 있는 기사가 있는데 이 결측치를 제거
df = df.drop(['_id'], axis=1)
# 이미지 기사 이외 NAN값 제거
df.dropna(inplace=True)
df.isnull().sum()
df.reset_index(drop=True, inplace=True)


from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

# TfidfVectorizer()를 이용하여 단어별 가중치 데이터를 추가함
tfidf = TfidfVectorizer()
tfidf_matrix = tfidf.fit_transform(df['content'])
n = len(df['content'])

# 코사인 함수 구하기 tfidf_matrix와 tfidf_matrix를  곱하여 코사인 함수를 구함
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

num = []
i = 0
j = 0
l = []
cosine_sim[i][j]
for i in range(n - 1):

    for j in range(1, n - 1):

        if cosine_sim[i][j] >= 0.8:

            if i < j: # i: 최신기사 j: i보다 먼저 나온 기사(나중기사)
                num.append(j) # j를 append함
                l.append([i, j])
                #print(i, j)
                #print(cosine_sim[i][j])

new_ = []
for v in num:
    if v not in new_:
        new_.append(v)
# new_리스트 값(중복된 기사 인덱스)을 drop
article = df.drop(index=new_)

# 몽고db에 넣기
my_articles = article.to_dict('records')
client = pymongo.MongoClient('mongodb:/[pw]/[ip]/')
articles = client.news.articles
articles.insert(my_articles)

#print(article)








