import json 

f=open("myfile.json","r")
ld=json.load(f)
print(ld)