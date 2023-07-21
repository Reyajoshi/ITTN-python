class Employee:
    def __init__(self,name,position):
        self.name=name
        self.position=position
    
    def greeting(self):
        print("Welcome to our company!")

class NewEmployee(Employee):
    def __init__(self,salary,name,position):
        self.salary=salary
        
        super().__init__(name,position)

    def worker(self):
        print(f"Name:{self.name}, Position:{self.position}, Salary:{self.salary}")


reya_object=NewEmployee(50000,"Ram","Senior employee")
reya_object.worker()
reya_object.greeting()



