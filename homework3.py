"""
@uthor:Abhishek Shekahr
HW 3
"""
print"Available Operations:"
print"add, sub, mult,division,all_even,all_odd, first_divisibleby_5,multi_table,area,volume"
while True:
    x=raw_input("enter your operation:")
    if x== "quit":
        print" thanks for using"
        break

    elif x=="add":
        num= raw_input("Enter two numbers separated by space:")
        num_list= num.split(" ") #splist a string by given argument
        b= int(num_list[0]) + int(num_list[1])
        print b
    elif x=="sub":
        num= raw_input("Enter two numbers separated by space:")
        num_list= num.split(" ") #splist a string by given argument
        b= int(num_list[0]) - int(num_list[1])
        print b
    elif x=="mult":
        num= raw_input("Enter two numbers separated by space:")
        num_list= num.split(" ") #splist a string by given argument
        b= int(num_list[0]) *int(num_list[1])
        print  b
    elif x=="division":
        num= raw_input("Enter two numbers separated by space:")
        num_list= num.split(" ") #splist a string by given argument
        b= float(num_list[0]) /float(num_list[1])
        print  b
    elif x=="all_even":
        num=input("Enter a number:")
        evens = [x for x in range(num) if x%2 == 0]
        print evens
    elif x=="all_odd":
        num=input("enter a number:")
        odd= [x for x in range(num) if x%2!=0]
        print odd
    elif x=="first_divisibleby_5":
        a=input("enter a number:")
        if a%5==0:
            print"Its divisible by 5"
        else:
             b=a/5
             c=5* (b+1)
             print c
    elif x=="multi_table":
        a=input("enter a number:")
        for c in range(1,11):
            print a,"X",c,"=",a*c
    elif x=="area":
        print "rectangle,circle,square,triangle"
        a=raw_input("enter the shape:")
        if a=="rectangle":
            l=float(input("enter length:"))
            b=float(input("enter breadth:"))
            area=l*b
            print "The area of rectangle is:",area,"sq.unit"
        elif a=="circle":
            r=float(input("enter radius:"))
            area = (22/7)*r**2
            print" The area of circle is:",area,"sq.unit"
        elif a=="square":
            l=float(input("enter length:"))
            area=l**2
            print"The area of sqaure is:",area,"sq.unit"
        elif a=="triangle":
             z = float(input('Enter first side: '))
             b = float(input('Enter second side: '))
             c = float(input('Enter third side: '))
             #calculate the semi-perimeter
             s = (z + b + c) / 2
             area = (s*(s-z)*(s-b)*(s-c)) ** 0.5
             print"The area of the triangle is:" , area ,"sq.unit"
    elif x=="volume":
        print"cylinder,cuboid,sqr_based_pyramid"
        b=raw_input("Enter the object:")
        if b=="cylinder":
            r=float(input("enter radius:"))
            h=float(input("enter height:"))
            vol=(22/7)*r**2*h
            print"The volume of cylinder is:",vol,"cubic unit"
        elif b=="cuboid":
            l=float(input("enter length:"))
            b=float(input("enter breadth:"))
            h=float(input("enter height:"))
            vol=l*b*h
            print"The volume of cuboid is:", vol, "cubic unit"
        elif b=="sqr_based_pyramid":
            l=float(input("enter length of square that is  base:"))
            h=float(input("enter height of pyramid:"))
            vol=(1/3.0)*l**2*h
            print"The volume of pyramid is:", vol , "cubic unit"
        else :
            print "unusual input"
        



            
            
                        
