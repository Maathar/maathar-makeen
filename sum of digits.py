digits=input("Enter a digits:")

def getSum(digits):
    sum = 0
    for d in str(digits): 
      sum =sum + int(d)      
    return sum
   

print(getSum(digits))