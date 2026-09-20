# s1 = ("H","E","A","R","T")
# s2 = ("E","A","R","T","H")

# if(sorted(s1) == sorted(s2)):
#     print("this is an angram: ")
# else:
#     print("THis is not!")

# print(sorted(s1))
# print(sorted(s2))

s3 = set(input("Enter any word:"))
s4 = set(input("Enter any word:"))

if(sorted(s3) == sorted(s4)):
    print("this is an angram: ")
else:
    print("THis is not!")


print(sorted(s3))
print(sorted(s4))