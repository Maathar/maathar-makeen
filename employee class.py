class employee:
    def __init__(self,emp_name,emp_id,emp_salary,emp_department):
        self.emp_name=emp_name
        self.emp_id=emp_id
        self.emp_salary=emp_salary
        self.emp_department=emp_department
        
    def calculate_emp_salary(self,salary,hours):
         overtime=hours-50
         if hours>250:
             self.emp_salary=salary+overtime
         else:
             self.emp_salary=salary
             
    def assign_department(self,new_emp_department):
         self.emp_department=new_emp_department       
        
    def emp_details(self):
        return "employee name is {},id:{},salary:{} and department:{} ".format(self.emp_name,self.emp_id,self.emp_salary,self.emp_department)
        
emp1=employee("Jones","E7499",450000,"research")
emp2=employee("Noor","E1249",1500,"IT")
emp3=employee("Ali","E1332",35400,"Math")

print(emp1.emp_details())
print(emp2.emp_details())
print(emp3.emp_details())
