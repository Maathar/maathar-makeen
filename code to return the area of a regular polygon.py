import math
n=input("Enter number of side :")
s=input("Enter side:")

def area (n,s):
    Area=(int(n)*float(s)**2)/(4*math.tan((22/7)/(int(n))))
    return  Area


print ("The area of poygon is:",area (n,s))



                   