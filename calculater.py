def add(a,b):
    c=a+b
    return c
#------------
def sub(a,b):
    c=a-b
    return c
#------------
def mult(a,b):
    c=a*b
    return c
#------------
def division(a,b):
    c=a/b
    return c
#---------
def even(a):
    evens = [x for x in range(a) if x%2 == 0]
    return evens
#----------
def odd(a):
    evens = [x for x in range(a) if x%2 != 0]
    return evens
#---------
def divis_5(a):
    if a%5==0:
        print "Its divisible by 5"
    else:
        b=a/5
        c=5* (b+1)
        return c

    




