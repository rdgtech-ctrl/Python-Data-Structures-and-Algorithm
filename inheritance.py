class Vehicle:
    def general_usage(self):
        print("general use: transportation")

# My Car class is derived/inherited from the Vehicle class
class Car(Vehicle):
    def __init__(self):
        print("I'm car")
        self.wheels = 4
        self.has_roof = True

    def specific_usage(self):
        self.general_usage()
        # if you don't make general_usage() function inside the Car it will take it from Vehicle class
        print("specific use: commute to work, vacation with family")

class MotorCycle(Vehicle):
    def __init__(self):
        print("I'm motor cycle")
        self.wheels = 4
        self.has_roof = True

    def specific_usage(self):
        print("specific use: road trip, racing")


c = Car()
m = MotorCycle()

print(isinstance(c,Car))
print(isinstance(c,MotorCycle))

print(issubclass(Car,Vehicle))
print(issubclass(Car,MotorCycle))
