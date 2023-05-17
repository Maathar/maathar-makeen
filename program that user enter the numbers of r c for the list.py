rows=int(input("enter number of rows:"))
column=int(input("enter number of columns:"))



a=[[i]*column for i in range(rows)]
  
for i in range(rows):
    for j in range(column):
        a[i][j]=int(input("enter the input"))
print(a,end="")
print()
    