color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
with open('text1.txt', "w") as myfile:
        for c in color:
                myfile.write("%s\n" % c)

content = open('text1.txt')
print(content.read())