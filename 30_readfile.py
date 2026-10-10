word = "dolor"
newline = "Hello bhaiyo kaise ho bhul to nhi gye hamka"

with open("log.txt", "a") as f:
    find = f.read()

findword = find.replace(word, "%%%%%%")

with open("log.txt", "w") as f:
    f.write(findword)