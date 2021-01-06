#Q3- Create a child class Bus that will inherit all of the variables and methods of the Vehicle Class and display it
'''
Given:

class Vehicle:
    def __init__(self, name, max_speed,mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
'''

class Vehicle:
    def __init__(self, name, max_speed,mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
   pass

B1 = Bus("Tata",170,15)

print("The Name of the Vehicle is :", B1.name)
print("The max_speed of the Bus is :", B1.max_speed)
print("The mileage of the Bus is :", B1.mileage)


