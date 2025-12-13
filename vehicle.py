class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
    
    def info(self):
        return f"Vehicle: {self.brand}, Year: {self.year}"

class Car(Vehicle):
    def __init__(self, brand, year, model):
        super().__init__(brand, year)
        self.model = model
    
    def info(self):
        return f"Car: {self.brand} {self.model}, Year: {self.year}"

vehicle = Vehicle("Ford", 2020)
print(vehicle.info())

car = Car("Toyota", 2022, "Camry")
print(car.info())

print(f"\nVehicle info: {vehicle.info()}")
print(f"Car info: {car.info()}")