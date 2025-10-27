class Vehicle:
    def __init__(self,b,mo,mi):
        self.brand=b
        self.model=mo
        self.mileage=mi
    def show_details(self):
        print(f"Brand : {self.brand}")
        print(f"Model : {self.model}")
        print(f"Mileage : {self.mileage}")
class Car(Vehicle):
    def __init__(self, b, mo, mi,ft):
        super().__init__(b, mo, mi)
        self.fuel_type=ft

    def show_details(self):
        super().show_details()
        print(f"Fule Type : {self.fuel_type}")

car1 = Car("Tata", "Nexon", 18, "Petrol")
car1.show_details()