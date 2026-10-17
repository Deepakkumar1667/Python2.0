information = '''Name : Deepak sharma,
Age : 21,
Course : BCA '''

with open("student.txt", "w") as f:
    f.write(information)


with open("student.txt", "a") as f:
    f.write("\nspecialization: Artificial intelligence")


with open("student.txt", "r") as f:
    info = f.readlines()
    total_line = len(info)


print(info)
print("total_line: ", total_line)

word = information.split()
print(len(word))


import string

text = ('''Python is easy.
I am learning Python.
PYTHON is useful.''').lower()

text = text.translate(str.maketrans("", "", string.punctuation))

with open("python.txt", "w") as f:
    f.write(text)

words = text.split()

total = words.count("python")

print(total)




search_word = input("Enter the word: ")

with open("log.txt", "r") as f:
    text = f.read()
    text = text.lower()

if search_word in text:
    print("word found!")
else: 
    print("word not found!")

print("in line no.: ",text.find(search_word))