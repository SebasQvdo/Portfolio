'''
Object Oriented Programming (OOP)
'''

class car:
    # initialize attributes, self refers to the class itself
    def __init__(self, brand, color):
        # assing values to attributes
        self.brand = brand
        self.color = color
    
    def honk(self):
        print("Beep beep!")
    
# Create an object of the class 'car'
my_car = car("Toyota", "Red")

print(my_car.brand)
print(my_car.color)
my_car.honk()



'''
Inheritance
'''

# The 'parent class'
class Animal:

    def __init__(self, name):
        self.name = name
    
    def move(self):
        print("Moving")

# Inherits from 'Animal' class, this being a 'child class'
class Dog(Animal):

    def bark(self):
        print("Woof!")

# Creating an instance of the 'Dog' class
my_dog = Dog("Buddy")

# Inherited attribute or behavior
print(my_dog.name)
my_dog.move()

# Specific behavior
my_dog.bark()



'''
Adding to Inheritance
'''

#parent class
class Animal:
    def __init__(self, name):
        self.name = name
    
    def move(self):
        print("Moving")
    # Generic sound method for any animal
    def sound(self):
        print("Making a sound")

#child class Dog
class Dog(Animal):
    def __init__(self, name, breed, age):
        # Initialize attributes of the parent class
        super().__init__(name)
        # Additional attrubutes specific to Dog
        self.breed = breed
        self.age = age

    # Overridden sound method for Dog
    def sound(self):
        print("Woof!")

#child class Cat
class Cat(Animal):
    def __init__(self, name, breed, age):
        super().__init__(name)
        self.breed = breed
        self.age = age

    # Overridden sound method for Cat
    def sound(self):
        # Call the sound method from Animal
        super().sound()
        # Additional functionality for Cat
        print("Meow!")

# Creating instances
my_dog = Dog("Buddy", "Golden Retriever", 5)
my_cat = Cat("Kitty", "Siamese", 3)

# Use overridden methods
my_dog.sound()
my_cat.sound()

#inherited attribute
print(my_dog.name)
print(my_cat.name)

#Additional attributes
print(my_dog.breed)
print(my_dog.age)
print(my_cat.breed)
print(my_cat.age)



'''
Polymorphism
'''

animals = [my_dog, my_cat]

#this way it can call the sound method of each object without knowing the specific class
for animal in animals:
    animal.sound()


'''
Example Problem
'''

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
class Ebook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size
    
my_ebook = Ebook("1984", "George Orwell", 10)
print(my_ebook.title)
print(my_ebook.author)
print(my_ebook.file_size, 'MB')


