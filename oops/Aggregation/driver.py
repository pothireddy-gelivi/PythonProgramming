class car:
    def __init__(self,cm,cc,cb):
        self.cmodel=cm
        self.ccolour=cc
        self.cbrand=cb
    
    def start(self):
        print(f"{self.cmodel} is started")
    
    def accelarate(self):
        print(f"{self.cmodel} is accelerated")

    def stop(self):
        print(f"{self.cmodel} is stopped")

class driver:
    def __init__(self,dn,da,de):
        self.dname=dn
        self.dage=da
        self.dexp=de

        cm=input("Enter the car model")
        cc=input("Enter the car colour")
        cb=input("Enter the car brand")
        CCOB=car(cm,cc,cb)
        self.dcar=CCOB
    def driver(self):
        print(f"{self.dname} is entered into the car")
        self.dcar.start()
        self.dcar.accelarate()
        self.dcar.stop()
        print(f"{self.dname} is come out of the car")

d1=driver("reddy",23,3)
d1.driver()