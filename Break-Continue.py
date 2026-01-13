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