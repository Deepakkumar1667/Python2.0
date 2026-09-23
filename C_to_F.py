#  Fehranhiet to celcious

def f_to_c(f):
    return 5*(f-32)/9

f = float(input("Enter temperature in F: "))
f_to_c(f)
print(round(f, 2),"°c")

# celcious to Fehranhiet

def c_to_f(c):
    return (c*9/5)+32

c = float(input("Enter temperature in F: "))
c_to_f(c)
print(round(c, 2),"°F")