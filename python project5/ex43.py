import csv
c_col = ['ID', 'Name', 'Age']
dict_data = [{'ID': 1, 'Name': 'Anu', 'Age': 1},
        {'ID': 2, 'Name': 'Abhina', 'Age': 15},
        {'ID': 3, 'Name': 'Anjaly', 'Age': 16},
        {'ID': 4, 'Name': 'Anagha', 'Age': 17},
        {'ID': 5, 'Name': 'Ann', 'Age': 18},
        {'ID': 6, 'Name': 'Annmary', 'Age': 19},
        {'ID': 7, 'Name': 'Anitta', 'Age': 20},
         {'ID': 8, 'Name': 'Aswathy', 'Age': 21},
         {'ID': 9, 'Name': 'Ardra', 'Age': 22},
        {'ID': 10, 'Name': 'Aparna', 'Age': 23}]
try:
    with open("name.csv", "r") as f:
        write = csv.DictWriter(f, fieldnames=c_col)
        write.writeheader()
        for i in dict_data:
            write.writerow(i)
except IOError:
    print("Input/Output Error")
d = csv.DictReader(open("name.csv"))
for i in d:
    print(i)


