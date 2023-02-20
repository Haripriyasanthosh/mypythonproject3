print("Enter the Name of Source File: ")
sFile = input()
print("Enter the Name of Target File: ")
tFile = input()

fileHandle = open("text1.txt", "r")
texts = fileHandle.readlines()
fileHandle.close()

fileHandle = open("text2.txt", "w")
for s in texts:
    fileHandle.write(s)
fileHandle.close()

print("\nFile Copied Successfully!")