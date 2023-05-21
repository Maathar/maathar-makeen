from datetime import date
class Person:
    def __init__(self,name,age,address,hours):
        self.name=name
        self.age=age
        self.address=address
        self.hours=hours
          
    def class_type(self):
        return "This is parent class"
    
class student(Person):
    def __init__(self,name,age,address,hours,grade):
        super().__init__(name,age,address,hours)
        self.grade=grade
        
    def class_type(self):
        return "This is student class"
    
    @classmethod
    def new_student(cls,name,birth_year,address,hours,grade):
        return cls(name,date.today().year- birth_year,address,hours,grade)
    
   
s1=student("salim",23,"muscat",180,[3.1,2.5,2])
p1=Person("salim",23,"muscat",180)
print(p1.class_type())
print(s1.class_type())
s1.new_student("salim",23,"muscat",180,[3.1,2.5,2])
s3=student.new_student("Ali",1933,"muscat",180,[3.1,2.5,2])
print(date.today()) 
print("The age of ",s3.name,"is",s3.age)




