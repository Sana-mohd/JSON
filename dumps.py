import json

a={
    "emp1": {
        "name": "Lisa",
        "designation": "programmer",
        1: "34",
        "salary": "54000"
    },
    "emp2": {
        "name": "Elis",
        "designation": "Trainee",
        2: "24",
        "salary": "40000"
    },
} 
mystring = json.dumps(a)
data=json.loads(mystring)

print(data)

