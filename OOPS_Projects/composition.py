
class Engine:
    def __init__(self,power,speed,torque):
        self.power = power
        self.speed = speed
        self.torque = torque

class Wheel:
    def __init__(self,material,size,weight):
        self.material = material
        self.size = size
        self.weight = weight

class Battery:
    def __init__(self,voltage,capacity):
        self.voltage = voltage
        self.capacity = capacity


class Car:
    def __init__(self,power,speed,torque,material,size,weight,voltage,capacity):
        self.engine = Engine(power,speed,torque)
        self.wheel = Wheel(material,size,weight)
        self.battery = Battery(voltage,capacity)

    def get_specification(self):
        print("\n ------ CAR SPECIFICATION ------ \n")
        print(" ------ Engine Details ------ \n")
        print("Engine Power:",self.engine.power)
        print("Engine Speed:",self.engine.speed)
        print("Engine Torque:",self.engine.torque)
        print("\n ------ Wheel Details ------ \n")
        print("Wheel Material:",self.wheel.material)
        print("Wheel Size:",self.wheel.size)
        print("Wheel Weight:",self.wheel.weight)
        print("\n ------ Battery Details ------ \n")
        print("Battery Voltage:",self.battery.voltage)
        print("Battery capacity:",self.battery.capacity)


# Test Case
car = Car("4.4L TwinPower Turbo V8","305 km/h","1,000 Nm","M light-alloy wheels","21 inches","2,940 kg","347.5 V","18.6 kWh")
car.get_specification()
