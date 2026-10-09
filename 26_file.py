# for write file

st = '''Hello i'm deepak sharma,
this is the secrat code - 123456789 '''
f = open("26.1_file.txt", "w")
f.write(st)

f.close()

# Read file 

f = open("26.2_file.txt", "r")
data = f.read()
print(data)

f.close()

#congrats code

conclusion = "Congrats! your learn this i/o function program"
f = open("26.3_ifle.txt", "w")
f.write(conclusion)

f.close()

# Readlines function

f = open("26.1_file.txt", "r")
lines = f.readlines()
print(lines, type(lines))

f.close()

# With function   
# Note: isme close() function lagane ki jarurt nhi hoti

code = '''Hey Mr. deepak sharma 
I'm giving you a secret code of my locker: 
tumhari yaadoo mai doobe sanam'''

with open("26.4_file.txt" , "w") as f:
    print(f.write(code))
    