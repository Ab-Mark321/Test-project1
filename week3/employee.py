class Employee:
    def __init__(self, name, salary):
        self.name = name          
        self.salary = salary      
    
    def annual_salary(self):
        return self.salary * 12   
        

emp = Employee("Alice", 3000)
print(f"Employee: {emp.name}")
print(f"Monthly salary: ${emp.salary}")
print(f"Annual salary: ${emp.annual_salary()}")


emp2 = Employee("Bob", 2500)
print(f"\n{emp2.name}'s annual salary: ${emp2.annual_salary()}")