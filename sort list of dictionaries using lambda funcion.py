people=[
    {'name':'John','age':28},
    {'name':'Mary','age':23},
    {'name':'Bob','age':35},
    {'name':'Alice','age':32}]

find_sort=sorted(people,key=lambda x: x['age'])
print(find_sort)


