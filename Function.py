# function 
# write a program of function to calculate sum of 2 no.  
def sum(a,b):  # parameters 
    s = a + b
    print("s = ",s)
    return s
sum(4,5) # fuction call

def prod(a = 4,b = 5):
    print(a * b)
    return a * b
prod()  

def prod(a,b = 5):  # Only non-default arguments can follow default argument.  
    print(a * b)    # reverse is not possible
    return a * b
prod()