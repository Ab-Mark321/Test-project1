# Car Class
class Car:
    def __init__(self, make):
        self.make = make  # Initialize the make attribute

    def get_make(self):
        return self.make  # Return the make


my_car = Car("Toyota")
print(f"Car make: {my_car.get_make()}")


another_car = Car("Honda")
print(f"other car make: {another_car.get_make()}")