import csv
with open("dep.csv",newline="")as f:
    d=csv.DictReader(f)
    print("magnitude subject")
    print("-----------")
    for i in d:
        print(i['magnitude'],i['subject'])