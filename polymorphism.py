class Animal:
    hello = "welcome"
    def sound(self,my_sound):
        print("My sound....", my_sound)
    
    # over loading
    def task(self,*args):
        print(args)   
    
    
    def welcome(self,hello):
        print(hello)

# method over riding
# with inheritance

class Cow(Animal):
    def welcome(self,hello):
        print("Welcome to program")
    
    
    
object = Animal()
object.sound("chirp")

cow_object = Cow()
cow_object.welcome("Hello")
cow_object.task("hi","hello",10,9)

'''
class Mammals:
    def __init__(self,name,species,habitat):
        self.name=name
        self.species=species
        self.habitat=habitat

    def make_sound(self):
        print("hello")

class Elephant(Mammals):
    def __init__(self,name,species,habitat,trunk):
        self.trunk=trunk
        super().__init__(name,species,habitat)
    def hello(self):
        print(f"Name:{self.name},Species:{self.species},Habitat:{self.habitat},Trunk:{self.trunk}")
    
    def make_sound(self):
        print("They make trumpeting sound")

class Bat(Mammals):
    def __init__(self,name,species,habitat,wing):
        self.wing=wing
        super().__init__(name,species,habitat)
    def hi(self):
        print(f"Name:{self.name},Species:{self.species},Habitat:{self.habitat},Wing:{self.wing}")

    def make_sound(self):
        print("They make echolocation sound")

class Giraffe(Mammals):
    def __init__(self,name,species,habitat,neck):
        self.neck=neck
        super().__init__(name,species,habitat)
    
    def hii(self):
        print(f"Name:{self.name},Species:{self.species},Habitat:{self.habitat},Neck:{self.neck}")
    def make_sound(self):
        print("They make hum sound")

elephant_object=Elephant('Elephant',3,"forest","extended nose")
elephant_object.hello()
elephant_object.make_sound()

bat_object=Bat('Bat',1400,"caves","Hand-wing")
bat_object.hi()
bat_object.make_sound()

giraffe_object=Giraffe("Giraffe",4,"grasslands","7feet")
giraffe_object.hii()
giraffe_object.make_sound()
'''




