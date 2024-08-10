class animal:
    def makesount(self):
        return f"meow"
class dog(animal):
    
    def makesound(self):
        return f"bark"
    
mydog = dog()
print(mydog.makesound())