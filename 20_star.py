'''
*
**
***
****
***** '''

# Star pattern
n = int(input("Enter a number: "))

for i in range(1, n+1):
    print("*"* i) 
    
print("")

''' ***
    * *
    *** '''
# Spacing pattern
n = int(input("Enter a number: "))

for i in range(1, n+1):
    if(i == 1 or i == n):
        print("*" * n , end="")
    else:
        print("*", end="")
        print(" " * (n-2), end="")
        print("*", end="")
    print("")


''' *****
    ****
    ***
    **
    *   '''
n = int(input("Enter a number: "))
for i in range(n, 0, -1):
    print("*" * i)

print("")


''' *****
    ****
    ***
    **
    *   '''
def star(n):
    if(n == 0):
        return
    print("*" * n)
    star(n-1)

star(10)