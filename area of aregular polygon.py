a=[22,3,-2,-1,10,1]
count=0
for element in a:
    print (element, end=" ")
   
    def getProduct(a):
        product = 1
        for d in a:
            product =product*d     
        return product
    
    if element<0:
        count+=1
 
print()   
print("The product of all element in list:",getProduct(a))
print("The number of element that is negative is",count)



    
