"""
Author:Abhishek Shekhar
hw 5-6-7
"""
f=open("input.txt" , 'r')
a = f.readline()
sum_1=0
sum_2=0
length=0
for i in f:
    b=i.split()
    e=float(b[0].strip())
    length=length+1
    sum_1=sum_1+e
    s=float(b[1].strip())
    sum_2=sum_2+s
mean1=sum_1/length
mean2=sum_2/length
#creating output.txt file
new_file=open("output.txt","w")
new_file.write("Mean_Temp      Mean_Humidity")
new_file.write("\n")
new_file.write (str(mean1)+ "  " +str(mean2))
new_file.close




    
