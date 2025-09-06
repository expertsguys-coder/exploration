# Parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")

# Child class inheriting from Animal
class Dog(Animal):
    def __init__(self, name, breed):
        # Call the parent's constructor
        super().__init__(name)
        self.breed = breed

    # Overriding the parent's method
    def speak(self):
        print(f"{self.name} the {self.breed} barks.")

# Creating objects
generic_animal = Animal("Generic Animal")
generic_animal.speak()

my_dog = Dog("Buddy", "Golden Retriever")
my_dog.speak()