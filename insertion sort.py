def insertionSort(lst):
    for i in range(1,len(lst)):
        key=lst[i]
        j=i-1
        while j>=0 and int(key.split(',')[1])< int(lst[j].split(",")[1]):
            lst[j+1]=lst[j]
            j-=1
        lst[j+1]=key
        
lst=["Said,25","Majid,19", "Salim,32", "Ali,21","Sultan,28"]
insertionSort(lst)
for i in range(len(lst)):
    print(lst[i],end="  ")