dec1={1:{"name":"p1","age":22},
      2:{"name":"p2","age":27} }

for item in dec1.items():
    age=item[1]["age"]
    if age>22:
        print(item[1]["name"])
