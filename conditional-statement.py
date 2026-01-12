# conditional statements. 
# if,elif,else
#Example 1:-
light = "green" 

if(light == "red"):
    print("stop")
elif(light == "green"):
    print("go")
elif(light == "yellow"):
    print("start")
else:
    print("light is broken")        

    print ("code is ended")
    
#Example 2:-
marks = int(input("enter a marks:"))

if(marks >= 90):
    print("grade A")
elif(marks >= 80 and marks < 90):
    print("grade B")
elif(marks >= 70 and marks < 80):
    print("grade C")
else:
    print("grade D")

    print("code is completed")             
