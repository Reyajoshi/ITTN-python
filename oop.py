'''
class MobilePhone: #in class we seperate by using capital letter instead of underscore
    new_phone="New model!"#we use methods(function)and attributes(variable)
    def phone(self):
        print(self.new_phone)
reya_object=MobilePhone()
reyan_object=MobilePhone()
reya_object.phone()#calling method of class MobilePhone in object
reyan_object.phone()
'''
'''
class HumanBeing():
    greet="Welcome to ITTN"
    def __init__(self,name):
        self.name=name
    def greeting(self):
        print(f"{self.greet},Name is:{self.name}")

reya_object=HumanBeing("Reya")
reyan_object=HumanBeing("Reyan")
reya_object.greeting()
reyan_object.greeting()
'''
'''
class Students():
    IT_training="Welcome new students in ITTN!"
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def training(self):
        print(f"{self.IT_training},Name is:{self.name},Age is:{self.age}")

ram_object=Students("Ram",19)
sita_object=Students("Sita",18)
laxman_object=Students("Laxman",20)
ram_object.training()
sita_object.training()
laxman_object.training()
'''
'''
class Competition():
    team="The score of"
    def __init__(self,name,score):
        self.my_name=name
        self.my_score=score
    def each_team(self):
        print(f"{self.team} {self.my_name} is {self.my_score}")
malpi_object=Competition("Malpi",120)
brihaspati_object=Competition("Brihaspati",150)
ace_object=Competition("Ace",110)
malpi_object.each_team()
brihaspati_object.each_team()
ace_object.each_team()
print("The winning team is Brihaspati")
'''
class ReyaJoshi:
    def __init__(self,age,height):
        self.age=age
        self.height=height

    def message(self):
        print("welcome everyone")

class Reya(ReyaJoshi):
    def __init__(self,legs,age,height):
        self.legs=legs

        super().__init__(age,height)
    
    def huhu(self):
        print(f"Age:{self.age},Legs:{self.legs},Height:{self.height}")

reya_object=Reya(2,19,5)
reya_object.huhu()
reya_object.message()
    
    