import json
f = open ("companyName.txt","r")
f.readline()
companies = []
while True:
	line =f.readline()
	if line:
		line = line.split("\t")
		#print line[1]
		if len(line)>1 and line[1]=='GSE ':
   			companies.append((line[2], line[0]))
	else:
		break
print companies
companyData = []
pk =1
for c in companies :
	companyData.append({"model":"stock.companie","pk":pk,\
	    "fields":{
            'companyName' : c[1],
            'companyIndex' : c[0],
            
	}
        })
        pk +=1

f.close()

f = open("companyList.json",'w')
f.write(json.dumps(companyData, indent=4))
f.close()
