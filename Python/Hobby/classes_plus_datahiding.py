'''
Example
'''

class Car:
  def __init__(self, model, year, odometer):
    self.model = model
    self.year = year
    self.odometer = odometer

  def describe_car(self):
    print(self.year, self.model)

  def read_odometer(self):
    print("Odometer:", self.odometer, "miles")

my_car = Car('Audi', 2020, 15000)

my_car.describe_car()
my_car.read_odometer()

#changing a value of the attribute
my_car.odometer = 20000

my_car.read_odometer()



'''
Data Hiding! - Protecting Attributes
'''

class Car:
    def __init__(self, model, year, odometer):
        self.model = model
        self.year = year
        #making odometer attribute protected
        self._odometer = odometer
    
    def describe_car(self):
        print(self.year, self.model)
    
    def read_odometer(self):
        print("Odometer:", self._odometer, "miles")

# But can still be accessed
my_car = Car('Audi', 2020, 15000)
my_car.read_odometer()

#accessing the protected attribute
print(my_car._odometer)


'''
Private Attributes...
'''

class Car:
    def __init__(self, model, year, odometer):
        self.model = model
        self.year = year
        # Making the odometer attribute 'private'
        self.__odometer = odometer
    
    def describe_car(self):
        print(self.year, self.model)
    
    def read_odometer(self):
        print("Odometer:", self.__odometer, "miles")

#my_car = Car('Audi', 2020, 15000)

# Accessing attribute 'within' method
#my_car.read_odometer()

# Error! - Trying to access private attribute from outside
#print(my_car.__odometer)



# Accessing private attribute using 'name mangling' to access them from outside
# The syntax is: object._class__private_attribute
my_car = Car('Audi', 2020, 15000)
print(my_car._Car__odometer)

'''
Protected and Private 'Methods'
'''

class Car:
  def __init__(self, model, year, odometer):
    self.model = model
    self.year = year
    # Making the odometer attribute 'private'
    self.__odometer = odometer  

  def _describe_car(self):  # Making the describe_car method 'protected'
    print(self.year, self.model)

  def __read_odometer(self):  # Making the read_odometer method 'private'
    print("Odometer:", self.__odometer, "miles")


my_car = Car('Audi', 2020, 15000)

#accessing protected method
my_car._describe_car()

#error when accessing a private method
#my_car.__read_odometer()