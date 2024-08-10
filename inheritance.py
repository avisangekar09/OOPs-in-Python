class vehicle:
    def __init__(self,make,year):
        self.make = make
        self.year = year
    def info(self):
        return f"{self.make} and {self.year}"
    
class bike(vehicle):
    def __init__(self,make,year,wheels):
        super().__init__(make,year)
         
        self.wheels = wheels
        
    def bikeinfo(self):
        return f"{self.make} and {self.year} and {self.wheels}"
    
mybike = bike("TVS",2001,2)
print(mybike.bikeinfo())
    