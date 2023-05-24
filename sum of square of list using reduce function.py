from functools import reduce


lis=[2,5,3,2]

sum=reduce(lambda y,x: y+x**2,lis,0)
print(sum)






