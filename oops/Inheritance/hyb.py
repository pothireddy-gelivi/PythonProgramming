class ElectricVehicle:
    def _init_(self, battery_capacity):
        self.battery_capacity = battery_capacity

    def display_battery(self):
        print(f"Battery Capacity: {self.battery_capacity} kWh")

class Vehicle:
    def _init_(self, brand):
        self.brand = brand

    def show_brand(self):
        print(f"Brand: {self.brand}")

class Car(Vehicle):
    def _init_(self, brand, model):
        super()._init_(brand, model)
        self.model = model

    def show_model(self):
        print(f"Model: {self.model}")

class SmartCar(Car, ElectricVehicle):
    def _init_(self, brand, model, battery_capacity, autonomous_level):
        Car._init_(self, brand, model)
        ElectricVehicle._init_(self, battery_capacity)
        self.autonomous_level = autonomous_level

    def show_all_info(self):
        self.show_brand()
        self.show_model()
        self.display_battery()
        print(f"Autonomous Level: {self.autonomous_level}")

my_smart_car = SmartCar("Tesla", "Model S", 100, "Level 4")

my_smart_car.show_all_info()