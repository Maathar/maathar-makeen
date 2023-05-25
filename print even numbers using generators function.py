lis=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
s=[]


def even (lis):
    for i in lis:
       if i %2==0:
            s.append(i)
    yield s
        
print(next(even(lis)))