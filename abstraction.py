class animal:
    def sound(self):
        pass
class cat(animal):
    def sound(self):
        return f"meow!"
mycat = cat()
print(mycat.sound())