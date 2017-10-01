"""
Author:abhishek shekhar
hw 4
"""
import random
x= [random.randint(0,255) for i in range(25)]
print x
print "**************************************************************"
"""
a=[x[i*5:i*5+5] for i in range(5)]
print a
"""
a=[]
for i in range(5):
    d=[]
    for j in range(5):
        d.append(x[j+i*5])
    a.append(d)
print a
    
#creating dictionary
dic={}
for i in range(5):
    #making key
    b="row"+str(i)
    if i!=0 and i!=4:
        dic[b]=(a[i][0],a[i][4])
print dic
print type(dic)
            
        
    

