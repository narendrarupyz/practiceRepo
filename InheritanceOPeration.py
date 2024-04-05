'''Inheritance: when you want to excute the functionality of another class is known as inhertance.
Sub Class: A class that inherit another class is known as sub Class.
Super Class or Base Class: A class that doesn't inherit from any other class is known as Super Class'''


#Super class or base class
class Vehicale():
    def description(self):
        print('I am Vehicale')

#sub class
class Car(Vehicale):
    pass

# create an object from each class
v = Vehicale()
c = Car()
v.description()
#I am Vehicale
c.description()
#I am Vehicale

#Override a Method: When a subclass provides its own custom implementation of a method that is already 
#provided by its base class, it is known as overriding.
class Vehicale():
    def description(self):
        print('I am Vehicale')

class Car(Vehicale):
    def description(self):
        print('I am Car')

v = Vehicale()
c = Car()

v.description()
#I am Vehicale
c.description()
#I am Car

#Add a Method: sub class can add additional methods that was not present in base class
class Vehicale():
    def description(self):
        print('I am a',self.color,' vehicale')

class Car(Vehicale):
    def description(self):
        print('I am a ', self.color, self.style)
    def setSpeed(self,speed):
        print('Now traveling at', speed, 'per mile')

v = Vehicale()
c = Car()

c.setSpeed(50)

#The super() Function: When you override a method, you sometimes want to reuse the method 
#of the base class and add some new stuff.
class Vehicale():
    def __init__(self,color):
        self.color = color
    def description(self):
        print('I am a ',self.color,' Vehicale')

class Car(Vehicale):
    def __init__(self, color,style):
        #invoking Vehicale's __init__() method
        super().__init__(color)
        self.style = style
    def description(self):
        print('I am a', self.color, self.style)

v = Vehicale('Red')
c = Car('Black','Suv')

c.description()
v.description()

#Multiple Inheritance: Python supports multiple inheritance, where sub class can Inherit
#from multiple super class.

class GroundVehicale():
    def drive(self):
        print('drive me on road')
class FlyingVehicale():
    def fly(self):
        print('fly me in sky')
class FlyingCar(GroundVehicale,FlyingVehicale):
    pass

fc = FlyingCar()
fc.drive()
fc.fly()


