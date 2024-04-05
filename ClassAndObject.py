'''Classes and Objects: A class is the blueprint from which individual objects are created. 
In Python, everything is an object integers, strings, lists, functions, even classes themselves.'''

#Create a Class
class Car:
    pass
#the pass statement is used to indicate that this class is empty.

#The __init__() Method: __init__() is the special method that initializes an individual object.
#This method runs automatically each time an object of a class is created.
class Car:
    def __init__(self):
        pass
#When you define __init__() in a class definition, its first parameter should be self.

#The self Parameter: The self parameter refers to the individual object itself.
# It is used to fetch or set attributes of the particular instance.

#Attributes: Every class you write in Python has two basic features: attributes and methods.
#There are two types of attributes: Instance attributes and Class attributes.

#Instance Attribute:
class Car:
    # initializer with instance attributes
    def __init__(self, color, style):
        self.color = color
        self.style = style

#Class Attribute:  class attribute is a variable that is same for all objects.
class Car:
    wheels = 4
# initializer with instance attributes
    def __init__(self, color, style):
        self.color = color
        self.style = style

#Create an Object: Create an object from the 'Car' class by passing style and color
class Car:
    def __init__(self, color, style):
        self.color = color
        self.style = style
#by Calling car class by passing arguments creating obj.
c = Car('Compact Suv','white')

#Access and Modify Attributes: The attributes of an instance are accessed and assigned to by using dot . notation.
class Car:
    def __init__(self, color, style):
        self.color = color
        self.style = style
c = Car('Black','Compact')
## Access attributes
print(c.style)
print(c.color)

# Modify attribute
c.style ='MUV'
print(c.style)

#Methods: Methods determine what type of functionality a class has, how it handles its data, and its overall behavior. 
#Instance Methods: Instance methods are nothing but functions defined inside a class that operates on instances of that class.

class Car:
    wheels = 4
    # initializer / instance attributes
    def __init__(self, color, style):
        self.color = color
        self.style = style
    
    # method 1
    def showDescription(self):
        print(F'Car color is {self.color} and style {self.style}')
    
    # method 2
    def changeColor(self, color):
        self.color = color

c = Car('red','Hatchback')

c.showDescription()
c.changeColor('Blue')

#Delete Attributes and Objects:
del c.color
del c

    





