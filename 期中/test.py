from sklearn import cluster, datasets
from sklearn.cluster import KMeans
import jieba
import csv
import numpy as np
punc = ["』","『","丨","｜","|","│","─","｜","－","—","〉","〈",">","<","&", "]", "[", "╱", "/", "0","０","1","１","2","２","3","３","4","４","5","５","6","６","7","７","8","８","9","９","。",".","；","=","●","%","【","】","《","》","：",":","+","?","？","!","！","，","," ,"「","　","」","＊","’",'"', " ","(",")","（","）","-","／","、"]
jieba.set_dictionary('\dict.txt.big.txt')

stopwords = []
with open('stoplist.txt', 'r', encoding='utf8') as txtFile:
    for data in txtFile.readlines():
        data = data.strip()
        stopwords.append(data)

corpus = {}
dic = {}
count_row = 0
count_corpus = 0
temp_cors = []
with open("flyingV_money (1).csv", "r", encoding="utf16") as csvFile:
    rows = csv.DictReader(csvFile, delimiter = "\t")
    for row in rows:
        dic[count_row] = []
        temp_title = ""
        for temp_word in row["title"]:
            if temp_word in punc:
                continue
            temp_title += temp_word
        words = jieba.cut(temp_title)
        if row["money"] >= row["targetmoney"]:
            continue
        for word in words:
            if word not in stopwords:
                dic[count_row].append(word)
                if word not in corpus:
                    temp_cors.append(word)
                    corpus[word] = 1
                    count_corpus += 1
                else: 
                    corpus[word] += 1
        count_row += 1


X = []

# Y = [0] * count_corpus
# X = []
# for row in range(count_row):
#     X.append(Y)


df_dic = {}
for word in temp_cors:
    temp = []
    for article in dic:
        if word in dic[article]:
            temp.append(article)
    df_dic[word] = temp

for word in df_dic:
    temp = []
    for article in dic:
        if word in dic[article]:
            temp.append(1)
        else:
            temp.append(0)
    X.append(temp)
X = np.array(X)

# for word in temp_cors:
#     # if corpus[word] < 5:
#     #     continue
#     print(word)
#     for article in dic:
#         for term in dic[article] :
#             if term == word:
#                 X[article][temp_cors.index(word)] = 1
#                 break
    

K = [3, 5]
# KMeans 演算法
for k in K:
    kmeans_fit = cluster.KMeans(n_clusters = k).fit(X.T)

    # 印出分群結果
    cluster_labels = kmeans_fit.labels_
    print("分群結果：")
    print(cluster_labels)
    print("---")

    np.savetxt(str(k) + "_result(failed).txt", cluster_labels)
# with open("result.txt", "w", encoding = "utf8") as result:
#     for i in cluster_labels:
#         result.write(i +"\n")

