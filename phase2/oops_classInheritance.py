# Pillars 0f Oops : Abstraction , Encapsulation, Inheritance, Ploymorphism
"""
DRY: Dont repeat Yourself


"""

#Inheritance: so lets say Employee, Client..but both has Person...cause..Employee has its salary detials....client has its related details..but..the person..is the common..on which is there for both.. like their..name, age...other details..

class Employee():
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary

    def increase_salary(self,percent):
        self.salary+=self.salary* (percent/100)


    def __str__(self):
        return f"the information: {self.salary}, {self.age}, {self.name}"

class Tester(Employee):
    #So if i increase the salary first it will check check..since its not there so it wil go to employee class
    def run_test(self):
        print(f"Testing is started by {self.name} ...")
        print("Test are done.")

class SlotsInspectoreMixin:
    def has_slots(self):
        return hasattr(self,"__slots__")


class Developer(SlotsInspectoreMixin,Employee):
    #over ride the new attributes

    def __init__(self,name, age, salary,framework):
        super().__init__(name,age,salary)
        self.framework=framework



    def increase_salary(self,percent,bonus=2):  # method overriding
        #self.salary+= self.salary *(percent/100)
        # so instead of writing the same thing..again..the calculation..we can use the super class
        super().increase_salary(percent)
        self.salary+=bonus


    def __str__(self):
        baseinfo= super().__str__()
        return f"{baseinfo} the extra info is: {self.framework}"






emp1= Tester("Lauren",23,1000)
emp2= Developer("mike",33,1200,"pthone")

emp1.increase_salary(20)
emp2.increase_salary(20,30)
print(emp1.salary)
print(emp2.salary)
print(emp1)
print(emp2)
print(emp2.has_slots())

#object class

print(isinstance(emp1, Tester))
print(isinstance(emp2,Employee))
print(issubclass(Developer, Employee))
print(issubclass(Employee, object))
print(issubclass(Developer,object))

print(emp2.__dict__)
print("__________")
#slots in python: Faster attribute access and reduced memory overhead
class Develop(SlotsInspectoreMixin):
    __slots__=("name","age","salary")

    def __init__(self,name, age, salary):
        self.name=name
        self.age=age
        self.salary=salary

empr1=Develop("ravi",34,30000)
print(empr1.__slots__)
print(empr1.has_slots())
print(Develop.__mro__)
# method resolution order


#Multiple Inheritance: one child class inherit from more than one parent class

