#write a program to input 2 number & print thier sum. 
a = int(input("enter a first number:"))
b = int(input("enter a second number:"))
sum = a+b
print (sum)

#write a program to input a side of a square & print its area. 
side = int(input("enter a value:"))
area = side * side 
print (area)

#write a program to input 2 floating number & print its avergae. 
a = float(input("enter a value:"))
b = float(input("enter a value:"))
print("average =",a+b/2)

# write a program to input a 2 integer value a & b print true if a is greater han equal to b. if not print false. 
a = int(input("enter a value:"))
b = int(input("enter a value:"))
print(a>=b)

# write a program to input user's first name & print ts length. 
name = input("enter a name:")
print("length of your name is",len(name))

# write a program to find the ocurrence of $ in a string. 
str = "i am a masterpiece of million $ & for selling for trillion $ " 
print(str.count("$"))
           
 

# write a program to check if number entered is even or odd. 

num = int(input("enter a number:"))
 
if(num % 2 == 0):
    print("number is even",num)
else:
    print("number is odd")    

# write a program to find the greatest of 3 numbers entered by the user. 

num1 = int(input("enter a first number:")) 
num2 = int(input("enter a second number:"))
num3 = int(input("enter a third number:"))

if(num1 >= num2 and num1 >= num3):
    print("first is greatest number",num1)
elif(num2 >= num3):
    print("second is greatest number",num2)    
else:
    print("third is greatest number",num3)    
# write a program to check if number is a multiple of 7 or not. 

num = int(input("enter a number:"))

if(num % 7 == 0):
    print("number is mltiple of 7")
else:
    print("number is not multiple of 7")    
 

# write a program to ask a user to enter names of 3 fav movies & store them into the list. 

movies = []
mov1 = input("enter a 1st movie :")
mov2 = input("enter a 2nd movie :")
mov3 = input("enter a 3rd movie :")

(movies.append(mov1))
(movies.append(mov2))
(movies.append(mov3))

print(movies)

#write a program to check if a list contain a palimdrome or not. 

list1 = [1,2,1]
list2 = [1,2,3]

copy_list1 = list1.copy
copy_list1.reverse()

if(copy_list1 == list1):
    print("palindrome")
else:
    print("not palindrome")    

#  write a program to count the number of student with grade A in following tuple. 
grade = ("C","D","A","A","B","B","A")
print(grade.count("A"))

# write a program to store a following word meanings in python dictionary. 
Dict = {
    "table" : ["a piece of furniture","list of facts & figures"],
    "cat" : "a small animal"
}
print(Dict)

#  problem statement. 
dict = {
    "python","java","c++","python","javascript","java","python","java","c++","c"
}
print(dict)
print(len(dict))

#write a program to enter a marks of 3 subjects from the user and store them in teh dictionary. start with a empty dictionary & add one by one.use subject name as key and marks as a value. 
marks ={}

a = input("enter a phy marks:")
print(marks.update({"phy marks" : a}))

b = input("enter a chem marks:")
print(marks.update({"chem marks" : b}))

c = input("enter a maths name:")
print(marks.update({"maths marks" : c}))

print(marks)

# figure out a way to store 9 & 9.0 as seperate value in set.(bcoz 9 & 9.0 is same and in set same cannot get repeatedly print.)
set = [9,"9.0"]
print(set)

# LOOP 
# While Loop 
count = 1
while count <= 5 :
    print("hello")
    count += 1


count = 1
while count <= 5 :
    print("hello",count)
    count += 1


# write a program to print a no. from 1 to 5.     
i = 1
while i <= 5:
    print(i)
    i += 1    


# write a program to print a no. from 5 to 1. 
i = 5
while i >= 1:
    print(i)
    i -= 1


# write a program to print a no. from 1 to 100. 
i = 1
while i <= 100:
       print(i)
       i += 1

# write a program to print a no. from 100 to 1.
i = 100
while i >= 1:
    print(i)
    i -= 1       

# print multiplication table of a number n.  
n = int(input("enter a number: "))
i = 1
while i <= 10:
    print(n*i)
    i += 1 


# print the square of the elements from 1 to 10.   
i = 1 
while i <= 10:
    print(i**2)
    i += 1 

# print the element of the following element list using a loop.
num = [1,4,9,16,25,36,49,64,100] 
idx = 0
while idx < len(num):
    print(num[idx])
    idx += 1

# Break 
i = 1
while i <= 5:
    print(i)
    if(i == 5):
        break
    i += 1 


# continue 
i = 0
while i <= 5:
    if(i==3):
        i += 1
        continue
    print(i)
    i += 1 
# if we want to print odd no. 
i = 0 
while i <= 10:
    if(i%2 == 0):
        i += 1
        continue
    print(i)    
    i += 1

# if we want to print even no.
i = 1
while i <= 10:
    if(i%2 != 0):
        i += 1
        continue
    print(i)    
    i += 1

# For Loop 
list = [1,2,3,4,5]
for num in list:
    print(num)  

tup = (1,2,3,4)
for num in tup:
    print(num)


# we can also print a else when we use break in loop.
tup = (1,2,3,4)
for num in tup:
    if(num == 3):
        break
    print(num)
else:
    print("End")    

# problem
list = [1,4,9,16,25,49,64,81,100]
for num in list:
    print(num) 

# problem
tup = (1,4,9,16,25,49,64,81,100,4)
x = 4
idx = 0
for num in tup:
    if(num == x):
        print("number found at idx",idx)
    idx += 1    


# range 

for i in range(2,100,2):   # range(start,stop,step) for even no. 
    print(i)
for i in range(1,100,2):   # for odd no.  
    print(i)


# print no. from 1 to 100. (using for and range)
for i in range(1,101):
    print(i)

# print no. from 100 to 1. (using for and range)    
for i in range(100,0,-1):
    print(i)

#print table of no. n 
n = int(input("enter a number:"))
for i in range(1,11,+1):
        print(n*i)


#pass statement. we create empty loop over here 
for i in range(5):
    pass

#WAP to find a sum of first n natural no.  
n = int(input("enter a number:"))
sum = 0
i = 1
while i <= n:
    sum  += i
    i += 1
print("total sum is:",sum)

#WAP to find a factorial. 

n = int(input("enter a number:"))
fact = 0
i = 1
while i <= n:
    fact  *= i
    i += 1
print("factorial is:",fact)


n = int(input("enter a number:"))
fact = 1
for i  in range (1,n+1,+1):
    fact *= i
print("factorial is:",fact)

# function 
# write a program of function to calculate sum of 2 no.  
def sum(a,b):  # parameters 
    s = a + b
    print("s = ",s)
    return s
sum(4,5) # fuction call

# average of 3 no. 
def avg(a,b,c):
    avg = (a+b+c)/3
    print("avg =",avg)
    return avg
avg(1,2,3)

# write a function to print the length of a list.
list1 = ["delhi","mussorie"]
list2 = ["capital","city"]
def print_len(list):
    print(len(list))

print_len(list1)
print_len(list2)

# write a function in one line. 
list1 = ["delhi","mussorie"]
list2 = ["capital","city"]
def print_len(list):
    print(len(list))

def print_list(list):
    for item in list:
        print(item, end=" ")

print_list(list2)        
print() 

# WAF of n factorial. 

def fact(n):
    fact = 1
for i in range(1,n+1,+1):
    fact *= i
    print(fact)
fact(5)