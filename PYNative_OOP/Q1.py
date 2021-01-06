# Q1 - Create a Vehicle class with max_speed and mileage instance attributes.

class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

V1 = Vehicle(145,35)
print("The max_speed of the Vehicle is :", V1.max_speed)
print("The mileage of the Vehicle is :", V1.mileage)