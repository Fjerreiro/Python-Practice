file = open(r"C:\Users\MedionTijmen\github\Python-Practice\Test Projects\Word Counter\wordlist.txt", "r")
data = file.read()
words = data.split()

print("The number of words in this file is: " + str(len(words)))
