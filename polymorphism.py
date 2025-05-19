class Animal:
    def __init__(self, name):
        self.name = name

    def move(self):
        print("This animal moves in a general way.")

class Dog(Animal):
    def move(self):
        print("Woof! Running on four legs.") 🐕

class Bird(Animal):
    def move(self):
        print("Chirp! Flying through the air.") 🐦

class Fish(Animal):
    def move(self):
        print("Glug glug! Swimming in the water.") 🐠

def animal_actions(animal):
    print(f"{animal.name}: ", end="")
    animal.move()

# Creating animal objects
dog = Dog("Buddy")
bird = Bird("Tweety")
fish = Fish("Nemo")

# Demonstrating polymorphism
animals = [dog, bird, fish]
for animal in animals:
    animal_actions(animal)
