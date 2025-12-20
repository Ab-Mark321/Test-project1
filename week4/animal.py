class Animal(ABC):
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
print(jasper.make_sound)