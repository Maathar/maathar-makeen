#print list by using nested for loop and if statement
a=[[i]*3 for i in range(4) if i>0]

print(a)

#print list by using nested for loop
a=[[i]*3 for i in range(1,4)]
  
for i in range(3):
    for j in range(3):
      print(a[i][j],end="")
    print()
    
