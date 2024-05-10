class Dog():
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + " says woof!"
    
class Cat():
    def __init__(self, name) -> None:
        self.name = name

    def speak(self):
        return self.name + " says meow!"
    

def pet_speak(pet):
    print (pet.speak())

dog = Dog('niko')
cat = Cat('felix')

pet_speak(dog)
pet_speak(cat)