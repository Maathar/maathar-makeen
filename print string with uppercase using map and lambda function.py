name=input("Enter a list of name seprated by commas:").split(",")
print("The list is:",name)

upper=list(map(lambda x: x.title(),name))
print("This is list with upperletter of fitrst letter:",upper)

u=list(map(lambda x: x.upper(),name))
print("This is list with upperletter of of all letter:",u)
