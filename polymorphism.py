class Cat:
    def speak(self):
        print("Meow!")

class Dog:
    def speak(self):
        print("Woof!")

class Cow:
    def speak(self):
        print("Moo!")

# A function that can take any object with a 'speak' method
def animal_speak(animal):
    animal.speak()

# Creating objects of different classes
my_cat = Cat()
my_dog = Dog()
my_cow = Cow()

# Using the same function with different objects
animal_speak(my_cat)
animal_speak(my_dog)
animal_speak(my_cow)