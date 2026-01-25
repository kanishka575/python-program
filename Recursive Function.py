def show(n):
    if(n==0):     # Base Case is like a stoping condition. 
        return
    print(n)
    show(n-1)

    show(5)


def show(n):
    if(n==-1): # recurssion will stop at 0. 
        return
    print(n)
    show(n-1)

    show(5)