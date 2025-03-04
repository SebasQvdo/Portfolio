'''
Class and Static Methods
'''

# There are different types of methods a class can have. The most common ones are:
# - Instance methods
# - Class methods
# - Static methods

'''
Class Methods
'''

class Book:
  def __init__(self, title, author):
    self.title = title
    self.author = author

  #regular method
  def describe_book(self):
    print(self.title, 'by', self.author)

  #class method
  @classmethod
  def books_in_series(cls, series_name, number_of_books):
    print('There are', number_of_books, 'books in the', series_name, 'series')

# Creating an instance of Book
my_book = Book("Harry Potter and the Sorcerer's Stone", "J.K. Rowling")

# Using the instance method to describe the book
my_book.describe_book()

# Using the class method to display information about the series
Book.books_in_series("Harry Potter", 7) #you dont need to create an instance of the class to use a class method

# calling the class method on the instance
my_book.books_in_series("Harry Potter", 7) #instances share everything with the class, meaning you can call class methods on instances



'''
Static Methods
'''

class Book:
  def __init__(self, title, author):
    self.title = title
    self.author = author

  #regular method
  def describe_book(self):
    print(self.title, 'by', self.author)

  #staticmethod, which dont recieve any additional arguments, they are just like regular functions
  @staticmethod
  def books_in_series(series_name, number_of_books):
    print('There are', number_of_books, 'books in the', series_name, 'series')

# Creating an instance of Book
my_book = Book("Harry Potter and the Sorcerer's Stone", "J.K. Rowling")

# Using the instance method to describe the book
my_book.describe_book()

# calling the static method
Book.books_in_series("Harry Potter", 7)


# Static methods can't alter the class's state or the instance's state, they are just like regular functions
# They are used when you want to group a function with a class, but the function doesn't need access to the class or instance


