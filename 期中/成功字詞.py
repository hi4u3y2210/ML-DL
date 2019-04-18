from sklearn import cluster, datasets
from sklearn.cluster import KMeans
import jieba
import csv
import numpy as np
punc = ["』","『","丨","｜","|","│","─","｜","－","—","〉","〈",">","<","&", "]", "[", "╱", "/", "0","０","1","１","2","２","3","３","4","４","5","５","6","６","7","７","8","８","9","９","。",".","；","=","●","%","【","】","《","》","：",":","+","?","？","!","！","，","," ,"「","　","」","＊","’",'"', " ","(",")","（","）","-","／","、"]
jieba.set_dictionary('C:\Program Files\Python36\lib\site-packages\jieba\dict.txt.big.txt')

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
    

K = [3,5]

dis_vec = {}
# KMeans 演算法
final_X2 = {}
count_member = {}
for k in K:
    dis_vec[k] = {}
    X2 = {}
    temp = []
    print(k)
    with open(str(k) + "_result(failed).txt", "r", encoding = "utf8") as txtFile:
        for row in txtFile:
            try:
                temp.append(int(txtFile.readline()[0]))
            except:
                continue
    # with open(str(k) + "_result(best).txt", "r", encoding = "utf8") as txtFile:
    #     for row in txtFile:
    #         try:
    #             temp.append(int(txtFile.readline()[0]))
    #             if temp[-1] not in dis_vec[k]:
    #                 dis_vec[k][temp[-1]] = []
    #             dis_vec[k][temp[-1]].append((final_X2[k][len(temp) - 1]))
    #             print(dic[len(temp) - 1])

    #         except:
    #             continue
    
    count_member[k] = []
    for i in range(k):
        count_member[k].append(temp.count(i))
    count = []
    for i in range(k):
        count.append(temp.count(i))
    for article in range(len(temp)):
        if temp[article] not in X2:
            X2[temp[article]] = {}
        for word in dic[article]:
            if word not in X2[temp[article]]:
                X2[temp[article]][word] = 1
            else:
                X2[temp[article]][word] += 1
    final_X2[k] = X2

for k in K:
    dis_vec[k] = {}
    temp = []
    print(k)
    with open(str(k) + "_result(failed).txt", "r", encoding = "utf8") as txtFile:
        for row in txtFile:
            try:
                temp.append(int(txtFile.readline()[0]))
                if temp[-1] not in dis_vec[k]:
                    dis_vec[k][temp[-1]] = []
                dis_vec[k][temp[-1]].append((X[len(temp) - 1]))
                # print(X[len(temp) - 1])

            except:
                continue
#distance
count_vector = 0
distance = {}
for k in dis_vec:
    distance[k] = {}
    temp_arr = []
    for clus in dis_vec[k]:
        sum_array = 0
        for vector in dis_vec[k][clus]:
            # print(len(vector))
            temp_arr.append((vector))
            count_vector += 1
        mean_vector = np.array(temp_arr).mean(0)
        # print(mean_vector)
        for vector in dis_vec[k][clus]:
            temp = vector - mean_vector
            for i in temp:
                sum_array += i**2
        sum_array /= count_vector
        distance[k][clus] = sum_array
print(distance)

final_score = {}
count_A = 0
for k in K:
    clus_score = {}
    for clus in range(k):
        score = {}
        for term in temp_cors:
            temp_score = 0
            ac = 0
            try:
                if term in final_X2[k][clus]:
                    ac = final_X2[k][clus][term]
            except:
                continue
            df = corpus[term]
            # for temp_class in range(k):
            #     if term in final_X2[k][temp_class]:
            #         df += final_X2[k][temp_class][term]
            #     if df == 0:
            #         print("AAAAAAAAAAAAA")
            #         count_A += 1
            ad = df - ac
            bc = count[clus] - ac

            bd = count_row - ad - ac - bc
            score[term] = temp_score
            a = ac + ad
            b = bc + bd
            c = ac + bc
            d = ad + bd
            T = a + b
            if ac>0:
                print(ac,ad,bc,bd, term)
                term_score = ((a*c)/T-ac)**2/((a*c)/T) + ((b*c/T-bc))**2/((b*c)/T) + ((a*d/T-ad))**2/((a*d)/T) + ((b*d/T-bd))**2/((b*d)/T)
                score[term] = term_score

        clus_score[clus] = score

    final_score[k] = clus_score
ss = []
# for k in final_score:
for clus in final_score[3]:
    for term in final_score[3][clus]:
        if final_score[3][clus][term] not in ss:
            ss.append(final_score[3][clus][term])
ss.sort()
# print(ss)
# print(final_score)
for k in K:
    print(k)
    for clus in final_score[k]:
        temp = []
        print(clus, end = "\t")
        print(count_member[k][clus])

        for term in final_score[k][clus]:
            temp.append(final_score[k][clus][term])
            # if ss[-1] == final_score[k][clus][term]:
            #     print(term)
            # if ss[-2] == final_score[k][clus][term]:
            #     print(term)
            # if ss[-3] == final_score[k][clus][term]:
            #     print(term)
        temp.sort()
        temp.reverse()
        temp_term = []
        for i in range(len(temp)):
            for term in final_score[k][clus]:
                if final_score[k][clus][term] == temp[i]:
                    temp_term.append(term)
                if len(temp_term) > 4:
                    break
            if len(temp_term) > 4:
                print(temp_term)
                break


# print(ss)
# print(count_A)
# print(final_score)

# for k in K:
#     kmeans_fit = cluster.KMeans(n_clusters = k).fit(X.T)

#     # 印出分群結果
#     cluster_labels = kmeans_fit.labels_
#     print("分群結果：")
#     print(cluster_labels)
#     print("---")

#     np.savetxt(str(k) + "_result(try).txt", cluster_labels)



# with open("result.txt", "w", encoding = "utf8") as result:
#     for i in cluster_labels:
#         result.write(i +"\n")

# 印出品種看看
# iris_y = iris.target
# print("真實品種：")
# print(iris_y)