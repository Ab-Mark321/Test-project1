from abc import ABC, abstractmethod
import json


'''class Employee:

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


show=FullTimeEmployee(4,400)
print(show.calculate_salary())'''


'''class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass


class dog(Animal):
    @property
    def make_sound(self):
        return "WOOF"

class cat(Animal):
    @property
    def make_sound(self):
        return "meow"


jasper=cat()
bobby=dog()
print(bobby.make_sound)
print(jasper.make_sound)'''

json_string='''
{ "list":[
    { "product":"laptop",
      "price":7500,
      "available":true
    }
    ]
    }
'''
data=json.loads(json_string)
print(data["list"])    