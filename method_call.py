'''
class HumanBeing:
    message="Welcome to ITTN!"#class variable
    a=5
    def __init__(self,name):
        self.my_name=name#instance variable
        self.height=5#instance variable

    #instance method
    def greet(self):
        print(f"{self.message} {self.my_name} {self.height}")
    
    #class method
    @classmethod
    def greetings(cls):
        print(f"{cls.message} {cls.a}")
    
    #static method
    @staticmethod
    def great():
        programming="Today we will learn python!"
        print(programming)
#instance way
reya_object=HumanBeing("Reya")
reya_object.greet()
reya_object.greetings()
reya_object.great()

#class way instance method cannot be called in class
HumanBeing.greetings()
HumanBeing.great()
'''
class NewIntern:
    message="Welcome!"
    group="You are gonna work with 10 other people"

    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.salary=15000
    def intern(self):
        print(f"{self.message},Name: {self.name},Age:{self.age},Salary:{self.salary}")

    @classmethod
    def internship(cls):
        print(cls.group)
    
    @staticmethod
    def words():
        advice="Work hard!"
        print(advice)

ram_object=NewIntern("Ram",21)
ram_object.intern()

NewIntern.internship()
NewIntern.words()






    