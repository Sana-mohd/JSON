import json

dict1 ={
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

out_file = open("myfile.json", "w")

json.dump(dict1, out_file, indent = 8)

out_file.close() 
