from abc import ABC, abstractmethod
import json

class Employee:

    @abstractmethod
    def calculate_salary(self):
        pass

    
class FullTimeEmployee(Employee):
    def __init__(self,workhours,salary):
        self.workhours=workhours
        self.salary=salary
    
    def calculate_salary(self):
        total= self.workhours*self.salary
        return total

emp=Employee()
print(emp.calculate_salary())
show=FullTimeEmployee(4,400)
print(show.calculate_salary())
