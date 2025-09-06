class Circle:
    pi = 3.14159  # Class attribute

    def __init__(self, radius):
        self.radius = radius

    # Instance method
    def area(self):
        return self.pi * self.radius ** 2

    # Class method
    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter / 2)

    # Static method
    @staticmethod
    def calculate_circumference(radius):
        return 2 * Circle.pi * radius

# Creating an instance using the constructor
c1 = Circle(5)
print(f"Area of circle with radius 5: {c1.area()}")

# Creating an instance using the class method
c2 = Circle.from_diameter(10)
print(f"Area of circle with diameter 10: {c2.area()}")

# Using the static method
print(f"Circumference of circle with radius 5: {Circle.calculate_circumference(5)}")