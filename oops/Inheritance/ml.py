class Country:
    def __init__(self,cn,c,p):
        self.country_name=cn
        self.continent=c
        self.population=p
    
    def show_country(self):
        print(f" Country : {self.country_name}")
        print(f" Continent : {self.continent}")

    def show_population(self):
        print(f"Population : {self.population}")

class State(Country):
    def __init__(self, cn, c, p,sn,cm,a):
        super().__init__(cn, c, p)
        self.state_name=sn
        self.chief_minister=cm
        self.area=a
    
    def show_state(self):
        super().show_country()
        print(f"State Name : {self.state_name}")

    def show_state_info(self):
        print(f"Chief Minister : {self.chief_minister}")
        print(f"Area : {self.area}")
class City(State):
    def __init__(self, cn, c, p, sn, cm, a,cityn,m,cp):
        super().__init__(cn, c, p, sn, cm, a)
        self.city_name=cityn
        self.mayor=m
        self.city_population=cp
    
    def show_city(self):
        super().show_state()
        print(f"City Name : {self.city_name}")

    def show_city_info(self):
        print(f"Mayor : {self.mayor}")
        print(f"City Population : {self.city_population}")

value=City("India","Asia","1,40,00,00,000","Andhra Pradesh","YS Jangan Mohan Reddy","1,60,000 sq km","Kadapa","XYZ","3,00,000")
value.show_state()
value.show_population()
value.show_state_info()
value.show_city_info()