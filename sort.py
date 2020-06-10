import csv

def readKeyValues():
	#input file reader
	infile = open("key-val.csv", "r")
	searchfile = open("key.csv", "r")
	read = csv.reader(infile)
	search = csv.reader(searchfile)
	headers = next(read) # skip header
	
	returnDictionary={}
	returnList=[]

	searchDictionary={}
	searchList=[]
	for query in search:
		searchList.append(query)
	
	#for each row
	for row in read:
		key   = row[0]
		value = row[1]
		
		#Add to dictionary (note, will overwrite and only store single occurrences)
		returnDictionary[key] = value
		
		#Add to list (note, will store multiple occurrences)
		returnList.append([key,value])
	
	#Now for the sorting	
	for i in searchList:
		for j in returnList:
			try:
				if i[0] == j[0]:
					print(j)
			#Don't die if a line skipped
			except IndexError:
				continue
readKeyValues()