def count_words(text1):
   with open(text1) as f:
       data = f.read()
       data.replace(",", " ")
       return len(data.split(" "))
print(count_words("text1.txt"))