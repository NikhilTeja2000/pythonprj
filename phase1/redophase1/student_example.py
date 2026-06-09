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

class StudentExample:

    def __init__(self,value):
        self.value=value
        self.students=[]

    def ask_names_marks(self):

        for a in range(self.value):
            student_name=input("Enter the your name: ")
            try:
                student_marks=list(map(int,input("enter your marks:").split(",")))
            except:
                print("Make sure.to enter integer use , to seperate")
            self.students.append({student_name:student_marks})
        #print(self.students)
        return len(self.students)

    def cal_grade(self):
        grades=[]
        for a in self.students:
            name,marks=list(a.items())[0]
            #print(name, sum(marks))
            grades.append(sum(marks))
        return grades

    def add_students_to_file(self):
        with open('students_marks.txt','w') as file:
            file.write(str(self.students))
        #print(os.getcwd())
        return os.path.abspath("students_marks.txt")




# so now this will run..when i run this file directly only.
if __name__ == "__main__":
    obw = StudentExample(2)
    print(obw.ask_names_marks())
    print(obw.cal_grade())
    obw.add_students_to_file()
