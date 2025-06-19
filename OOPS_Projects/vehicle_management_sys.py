from abc import ABC,abstractmethod

class Vehicle(ABC):
    def __init__(self,engine_no,brand,model,owner):
        self.__engine_no = engine_no
        self.brand = brand
        self.model = model
        self.owner = owner
    
    @abstractmethod
    def start_engine(self):
        pass
    
    @abstractmethod
    def get_details(self):
        pass

class Car(Vehicle):
    def __init__(self, engine_no, brand, model, owner, num_doors, boot_space, air_bags):
        super().__init__(engine_no, brand, model, owner)
        self.doors = num_doors
        self.boot_space = boot_space
        self.air_bags = air_bags

    def start_engine(self):
        print("\n Engine Started.... \n")

    def get_details(self):
        print("Owner Name :",self.owner)
        print("Brand Name :",self.brand)
        print("Model :",self.model)
        print("Number of Doors :",self.doors)
        print("Air Bags :",self.air_bags)
        print("Boot Space :",self.boot_space)

class Bike(Vehicle):
    def __init__(self, engine_no, brand, model, owner, kick_start, type, helmet_included):
        super().__init__(engine_no, brand, model, owner)
        self.has_kick_start = kick_start
        self.type = type
        self.helmet_included = helmet_included

    def start_engine(self):
        print("\n Engine Started.... \n")

    def get_details(self):
        print("Owner Name :",self.owner)
        print("Brand Name :",self.brand)
        print("Model :",self.model)
        print("Kick Start :",self.has_kick_start)
        print("Bike Type :",self.type)
        print("Helmet Included :",self.helmet_included)

class Truck(Vehicle):
    def __init__(self, engine_no, brand, model, owner, load_capacity, num_wheels, trailer_attached):
        super().__init__(engine_no, brand, model, owner)
        self.load_capcity = load_capacity
        self.num_wheels = num_wheels
        self.trailer_attached = trailer_attached

    def start_engine(self):
        print("\n Engine Started.... \n")

    def get_details(self):
        print("Owner Name :",self.owner)
        print("Brand Name :",self.brand)
        print("Model :",self.model)
        print("Loading Capacity :",self.load_capcity)
        print("Number of Wheels :",self.num_wheels)
        print("Trailer Attached :",self.trailer_attached)
