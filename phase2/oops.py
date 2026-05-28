from os import name

"""

**Fun Textbook Fact:** The word `self` is actually **not** a reserved keyword in Python! It is just a strong community convention. You could technically name it `banana` or `me` (e.g., `def __init__(me, name):`), and Python would run it perfectly fine because it only cares that the *first parameter* points to the object. However, if you use anything other than `self`, other programmers will look at you very weirdly!
"""
class Employee:

    def __init__(mango,name, age, position , salary): #so its responsible for initialising the new object... so the arugments are recieved as the parameters here.
        mango.name= name
        mango.age=age
        mango.position=position
        #mango.set_salary(salary) so now we are not using the custom setter
        mango.salary=salary




    def increase_salary(mango,cost):
        print( f'Hi {mango.name} your salary has been increased so is your current salary is: {mango.salary}? am i right?')
        mango.salary+=10000+cost
        return mango.salary
    def __str__(self): #so it take the instance..
        return f'Hi, {self.name} so your current salary is :{self.salary} and  your age is {self.age}'
    def __repr__(self): #so it represents..in more formal way...it was mostly used by the developer not the end users.
        return f'Employee, {repr(self.name)} so your current salary is : {repr(self.salary)} and  your age is {repr(self.age)}'

    def __add__(self, other):
        return Employee("temp",33,"combined",self.salary+other.salary)
        #return self.salary + other.salary-

    """def get_salary(self):
        return self._salary
"""


    @property
    def salary(self):
        return self._salary
    #python decorator concept...
    @salary.setter
    def salary(self,salary):
        if salary<10000:
            raise ValueError('Min wage is $1000')
        self._annual_salary=None
        self._salary=salary # so here if we remvoe the underscore we would get the max recurrsio depth exceeded error cause..because we would accidentally trigger the setter function over and over again in an endless loop.

    """
        def set_salary(self,salary):
        if salary<1000:
            raise ValueError("mininum wage is $1000")
        self._salary=salary
    
    """
    # so this is the computed property.so it returned the results of the computation of the same instamce...so its only calcuated..when we need to access it.
    @property
    def annual_salary(self):
        return self.salary* 12








s= Employee("raji",22,"2030",40000)

s2= Employee("ram",32, "whope",30000)

s3= Employee("nikhil",32, "hight",40000)
s4= Employee("raju",32, "hight",50000)
s5= Employee("teja",32, "hight",40600)
s6= Employee("akhil",32, "hight",20000)



print(s.name)
print(s)
print(s2.position,s2._salary,"so in one place i passed the int one i passed the string",s.position, s._salary)
print(s2.increase_salary(30))
print(s2)

print(repr(s2))
#print(eval(repr(s2))) #gives error..cause..we have written tthe strings so we are evaluation..so it tries to run the ..but when..it sees the strings..it break...
print("_______________")
# Dunder method

print(s2.__dict__)
print(s2.__class__)
print("lets see:----")
print(s2+s3)
print(s2+s3+s4+s5+s6) #so to fix this..i need to pass the object only during the add so that it will add those two..right..
# so operator overloading..so its like when you use the + in python it would goes to the __add__

#Managing Attributes
#s2.set_salary(100000)
#print(s2.get_salary())
s2.salary=200000
print(s2.salary)

#user_input=int(input("input salary: "))
#if user_input<1000:
 #   raise ValueError("Minimum wage is $1000 dollars")
#else:
 #   s2.salary=user_input

# above code is correct..but if we want to check mulitple times...it would not be good enough..its like

#Pillars of OOP
"""
Abstraction: displaying only the basic infor and hiding the implementaiont...
class instances should hide the implementation details
Users only need to have the interface


Encapsulation: fist class should be able to ..or its like its groupd realted adata and methods..
hiding of the data attribites which are only used for internal implementation purposes


Name mangling so now we need to use the __ so they cannot access that outside of the class..but they can still access but its little complex.
"""
#print(s3.get_salary())
print(s3.salary)


# so now the code has two things one is the salary another one is _salary so to fix that i changed every thing to _salary
# but the good way properties


# Using Computed Properites
print(s2.annual_salary)


#Same emp example..
class Employed():

    def __init__(self,salary):
        self.salary= salary

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self,value):
        if value<0:
            raise ValueError("Salary cannot be -ve")
        self._salary=value




e1=Employed(5000)
print(e1.salary)
