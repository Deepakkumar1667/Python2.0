# First method
# 1 x 2 x 3 x 4 x 5 = 120 
n = int(input("Enter a number: "))

factorial = 1 
for i in range(1, n+1):
    fact *= i

print(factorial)



# Second method
# 5 x 4 x 3 x 2 x 1 = 120
def factorial(n):
    if(n==0 or n==1):
        return 1
    return n * factorial(n-1)

n = int(input("Enter a number: "))
print(factorial(n))