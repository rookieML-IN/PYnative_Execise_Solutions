#Q5. Define property that should have the same value for every class instance
'''
Define a class attribute "color" with a default value "white". i.e. Every Vehicle should be white.

Use the following code for this exercise.

class Vehicle:
    def __init__(self, name, max_speed,mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass
'''
class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def color(self, color = "White"):
        return color


class Bus(Vehicle):
    pass


class Car(Vehicle):
    pass

publicBus = Bus("School VOLVO", 180, 12)
perCar = Car("Audi Q5", 240, 18)

print("Color :", publicBus.color(), "Speed :", publicBus.name, "Mileagae :", publicBus.mileage)
print("Color :", perCar.color(), "Speed :", perCar.name, "Mileagae :", perCar.mileage)