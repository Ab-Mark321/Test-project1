class Person:
    def __init__ (self, name , age):
        self.name=name
        self.age=age
    @property   
    def me(self):
        return f"my name is {self.name} and i am {self.age}"

person1=Person("Abenezer",20)
print(person1.me)

