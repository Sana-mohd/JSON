a={
    '4': 5, 
    '6': 7, 
    '1': 3, 
    '2': 4}
b={}
for i,j  in sorted(a.items()):
    b[i]=j
#print(b)

import json
f=open("sorted_keys.json","w")
z=json.dump(b,f,indent=4)
f.close()