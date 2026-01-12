student =  {
    "name" : "rohit",
    "subject" : {
        "phy" : "1",
        "chem" : "2",     
        "maths" :"3",
    }
}
print(student)
print(student["subject"])
print(dict.keys())  # return all keys 
print(dict.values())  # return all the values
print(len(student))   # it tell us the no. of keys in it. 
print(student.items()) # it return the (keys,values) as pair of tuples. 
print(student.get("key")) # it return the key according to value. 
student.update({"exam" : "19"}) # it add new dictionary into existing one. 
print(student)