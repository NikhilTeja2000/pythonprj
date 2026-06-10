"""
1. Ask student name
2. Ask marks
3. Calculate grade
4. Store student as dictionary
5. Add multiple students into a list
6. Use function to calculate grade
7. Use try/except for invalid marks
8. Write final students to a file
"""
import os
from abc import ABC, abstractmethod



class StudentExample:

    #class variable
    school_name='Viveka'

    def __init__(self,value):
        self.value=value
        self._students=[]

    def add_students(self,name,marks):
        self._students.append({name:marks})

    def get_students(self):
        return self._students



    #instance methods
    def ask_names_marks(self):

        for a in range(self.value):
            student_name=input("Enter the your name: ")
            try:
                student_marks=list(map(int,input("enter your marks:").split(",")))
                self._students.append({student_name:student_marks})
            except:
                print("Make sure.to enter integer use , to seperate")

        #print(self._students)
        return len(self._students)

    def cal_grade(self):
        grades=[]
        for a in self._students:
            name,marks=list(a.items())[0]
            #print(name, sum(marks))
            #grades.append(sum(marks))
            grades.append(self.cal_marks(marks))

        return grades


    @staticmethod
    def cal_marks(marks):
        return sum(marks)

    @classmethod
    def change_school_name(cls, name):
        cls.school_name = name


class FileManager:
    def write_to_file(self,file_name,data):
        with open(file_name+'.txt','w') as file:
            file.write(str(data))
        return os.path.abspath(file_name+'.txt')


#before we are doing the inheritance..passing only one which is Student Example but now..i am passing the File Manager also
# and one more concept here which is MRO: which is since we wrote the student example first..so if both class has same method name it will call the first one we wrote here ..which is student example
class StudentReport(StudentExample, FileManager):

    def __init__(self,value,file_name):
        super().__init__(value)
        self.file_name=file_name

    #Method Overriding
    def cal_grade(self):
        grades=[]
        for a in self._students:
            name,marks=list(a.items())[0]
            #print(name, sum(marks))
            #grades.append(sum(marks))
            grades.append(self.cal_marks(marks))
        grades.sort(reverse=True)
        return grades

    def add_students_to_file(self):
        # with open(self.file_name+'.txt','w') as file:
        #     file.write(str(self._students))
        # #print(os.getcwd())
       # return os.path.abspath(self.file_name+'.txt')
        return self.write_to_file(self.file_name,self.get_students())

#polymorphism: so i can pass any obj based on that it will call its related parent one or the child one...
def show_grades(objects):
    print(objects.cal_grade())



# so now this will run..when i run this file directly only.
if __name__ == "__main__":
    # obw = StudentExample(2)
    # print(obw.ask_names_marks())
    # print(obw.school_name)
    # obw.change_school_name("Chait")
    # print(obw.school_name)
    # print(obw.cal_grade())
    #obw.add_students_to_file() now this cant be done..cause we moved this to the child class.

    # so now i created an object from the child class and accessed the parent class also.
    report = StudentReport(2,"Student_text")

    print(report.ask_names_marks())
    print(report.school_name)
    report.change_school_name("Donebosco")
    print(report.school_name)
    #print(report.cal_grade())
    show_grades(report)
    report.add_students_to_file()