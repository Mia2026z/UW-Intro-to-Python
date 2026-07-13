class Car:
    def drive(self, speed_increase):
        self.speed += speed_increase

# Review methods, classes, and objects


class Car:
    def __init__ (self, brand, color):
        self.brand = brand
        self.color = color
        self.__speed = 0

    def drive(self, amount):
        self.__speed += amount


class SportsCar(Car): # Inherits from Car
    def __init__ (self, brand, color, turbo):
        super().__init__(brand,color) # Call parent class constructor
        self.turbo = turbo




class Pet:
    def __init__ (self, name, type):
        self