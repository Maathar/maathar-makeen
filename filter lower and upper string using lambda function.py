string=["cat","DOG","WATER","pin"]
u=list(filter(lambda char: char.isupper(),string))
l=list(filter(lambda char: char.islower(),string))
print(string)
print(u)
print(l)