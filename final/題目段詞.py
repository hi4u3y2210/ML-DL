import csv
import gc
skipChars = set(["0","０","1","１","2","２","3","３","4","４","5","５","6","６","7","７","8","８","9","９","。",".","；","=","●","%","【","】","《","》","：",":","+","?","？","!","！","，","," ,"「","　","」","＊","’",'"', " ","(",")","（","）","-","／","、","a","A","b","B","d","D","e","E","f","F","g","G","h","H","k","K","l","L","m","M","o","O","p","P","q","Q","r","R","s","S","t","T","u","U","v","V","w","W","x","X","y","Y","z","Z"])
ranktf = {}
rankdf = {}
dellist = []
docucount = 0
path_question_data = ".csv"
n = input("請輸入文章代號: ")
with open(path_question_data, "r", encoding = "utf16") as csvfile:
	print("Open Successful")
	a = csv.DictReader(csvfile, delimiter = "\t")

	for i in a:
		if i["編號"] != n:
			continue	
		slice = (i["標題"] + "." + i["內容"])
		gram = []	
		for k in range(len(slice) - 1):
			for j in range(2, 7):
				if j + k <= len(slice):
					word = slice[k:k+j]
					if len(set(set(word) & skipChars)) > 0:
						break
					gram.append(word)		
				else:
					break
		break

save = []
path_all_dict = ".csv"
with open(path_all_dict, "r", encoding = "utf16") as csvfile:
	print("Open Successful")
	a = csv.DictReader(csvfile, delimiter = "\t")
	for i in a:
		if i["gram"] in gram:
		    save.append(i)

print("Writing File")

with open("result.txt", "w", encoding="utf16") as result:		
	for i in save:
		result.write(i["gram"] + "\t" + i["tf"] + "\t" + i["df"] + "\t" + i["全部tf"] + "\t" + i["全部df"] + "\n")
		
print("Done")


