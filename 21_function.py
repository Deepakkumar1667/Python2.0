def avg():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    c = int(input("Enter third number: "))

    average = (a+b+c)/3
    print(average)

avg()
print("Thank you!")
avg()
print("Thank you!")
avg()
print("Thank you!")
avg()
print("Thank you!")
avg()
print("Thank you!")
avg()
print("Thank you!")



def sum(n):
    if(n == 1 ):
        return 1
    return sum(n-1) + n

print(sum(4))


def full_name(name, ending="sharma"):
    print("Hello Mr.",name,ending)

full_name("Deepak")