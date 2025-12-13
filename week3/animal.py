class Animal:
    def make_sound(self):
        return "Some generic animal sound"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

animal = Animal()
print(f"Animal says: {animal.make_sound()}")

cat = Cat()
print(f"Cat says: {cat.make_sound()}")

print(f"Is cat an Animal? {isinstance(cat, Animal)}")
print(f"Is cat a Cat? {isinstance(cat, Cat)}")
print(f"Is animal a Cat? {isinstance(animal, Cat)}")