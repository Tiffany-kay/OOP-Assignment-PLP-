# Base class
class Animal:
    def move(self):
        pass  # Placeholder for derived class implementations


# Derived class representing a Dog
class Dog(Animal):
    def move(self):
        return "The dog runs on four legs 🐕"


# Derived class representing a Bird
class Bird(Animal):
    def move(self):
        return "The bird flies in the sky 🐦"


# Derived class representing a Fish
class Fish(Animal):
    def move(self):
        return "The fish swims in water 🐟"


# Creating instances of the Animal subclasses
dog = Dog()
bird = Bird()
fish = Fish()

# Demonstrating polymorphism
print(dog.move())
print(bird.move())
print(fish.move())
