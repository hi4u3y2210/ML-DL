import csv
import gc
skipChars = set(["0","０","1","１","2","２","3","３","4","４","5","５","6","６","7","７","8","８","9","９","。",".","；","=","●","%","【","】","《","》","：",":","+","?","？","!","！","，","," ,"「","　","」","＊","’",'"', " ","(",")","（","）","-","／","、","a","A","b","B","c","C","d","D","e","E","f","F","g","G","h","H","i","I","j","J","k","K","l","L","m","M","n","N","o","O","p","P","q","Q","r","R","s","S","t","T","u","U","v","V","w","W","x","X","y","Y","z","Z"])
ranktf = {}
rankdf = {}
dellist = []
docucount = 0
path_news_data = ".csv"
with open(path_news_data, "r", encoding = "utf16") as csvfile:
	print("Open Successful")
	a = csv.DictReader(csvfile, delimiter = "\t")

	d = 0
	for i in a:
		slice = (i["標題"] + "." + i["內容"])
		d += 1
		key = 0
		save = {}	
		for k in range(len(slice) - 1):
			for j in range(2, 7):
				if j + k <= len(slice):
					word = slice[k:k+j]
					if len(set(set(word) & skipChars)) > 0:
						break
					ranktf[word] = ranktf.get(word, 0) + 1
					save[word] = save.get(word, 1)	
						
				else:
					break
		for k in save:
			rankdf[k] = rankdf.get(k, 0) + 1
			

print("相同字詞篩選")

for i, j in ranktf.items():
	if j < 50:
		dellist.append(i)
for i in dellist:
	ranktf.pop(i, None)
	rankdf.pop(i, None)
dellist = []		
counter = 0
for k in range(2, 6):
	savestring = ""
	pendingDelete = []
	for i in ranktf:
		if len(i) == k:
			counter += 1
			if counter > 1:
				if savestring[1:-1] == i[0:-2]:
					if abs(ranktf[i] - ranktf[savestring]) < 50:
						pendingDelete.append(i)
						pendingDelete.append(savestring)
					
				savestring = i
			else:
				savestring = i
	counter = 0		
	for word in pendingDelete:
		ranktf.pop(word, None)
		rankdf.pop(word, None)
savek = ""
savev = 0
for k, v in ranktf.items():
	if abs(v - savev) < 50 and len(k) != len(savek):
		if len(savek) > len(k):
			dellist.append(k)
		else:
			dellist.append(savek)
	
	savek = k
	savev = v
for i in dellist:
	ranktf.pop(i, None)
	rankdf.pop(i, None)
dellist = None
gc.collect()
print("Writing File")


with open("result.txt", "w", encoding="utf16") as result:		
	result.write(str(docucount) + "\n")
	for k, v in ranktf.items():
		if k in ranktf:
			result.write(str(k) + "\t" + str(v) + "\t" + (rankdf[k]) + "\n")
		
print("Done")


