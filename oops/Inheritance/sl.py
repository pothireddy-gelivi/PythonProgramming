class Device:
    def __init__(self,b,m):
        self.brand=b
        self.model=m
    
    def show_device_info(self):
        print(f"Brand : {self.brand}")
        print(f"Model : {self.model}")

class Smartphone(Device):
    def __init__(self, b, m,r,s,p):
        super().__init__(b, m)
        self.ram=r
        self.storage=s
        self.price=p
    def show_smartphone_info(self):
        super().show_device_info()
        print(f"Ram : {self.ram}")
        print(f"Storage : {self.storage}")
        print(f"Price : {self.price}")

Samsung = Smartphone("Samsung", "Galaxy S24", "12GB", "256GB", "₹85,000")
Samsung.show_smartphone_info()