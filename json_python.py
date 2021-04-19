import json
a={"Name":"Ram", 
     "Class":"IV", 
     "Age":9 }

f=open("convert.json","w")
json.dump(a,f,indent=2)
f.close()