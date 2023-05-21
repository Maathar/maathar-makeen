class Person:
    no_of_persons= 0
    def __init__(self,name,age):
        self.name=name
        self.age=age
        Person.no_of_persons +=1
    def __str__(self):
        return "This person name is {} and {} years old".format(self.name,self.age)
    
p1= Person("Hamza",22)
p2=Person("Ali",23)
print(p1.__str__())
print(p2.__str__())
print(Person.no_of_persons)