#Q7. Determine which class a given Bus object belongs to (Check type of a Object)
"""
Given:
class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

class Bus(Vehicle):
    pass

School_Bus = Bus("School Volvo", 12,50)
"""


class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity


class Bus(Vehicle):
    pass

School_Bus = Bus("School Volvo", 12, 50)
print(type(School_Bus))