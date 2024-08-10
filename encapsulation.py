#print("hello world")

class car:
    def __init__(self,make,year):
        self.__make = make
        self.year = year
        
    def info(self):
        return f"{self.__make} and {self.year} of car"
    
    def getname(self):
        return self.__make
    
    def setname(self,make):
        self.__make = make
        
mycar = car("suzuki",2001)

print(mycar.getname())
print(mycar.info())
