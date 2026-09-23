# By Recursion Method 

def factorial(n):  # creating a function 
    if(n == 1 or n == 0):  # local breakig function 
        return 1
    return n * factorial(n-1)   # return value based on formula 

n = int(input("Enter a number: "))  # user input
print(factorial(n))   # function calling 

# 5 x 4 x 3 x 2 x 1 = 120  