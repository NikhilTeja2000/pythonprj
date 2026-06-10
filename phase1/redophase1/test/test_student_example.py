import unittest
from phase1.redophase1.student_example import StudentExample

class MyTestCase(unittest.TestCase):

    def test_add_student_marks(self):
        #arrange
        value=StudentExample(2)
        #act
        answer=value.ask_names_marks()
        #assert
        self.assertEqual(answer,2)

    def test_grades_students(self):
        #arrange
        value=StudentExample(2)
        #value.students=[{"Nikhil": [2, 3]},
         #               {"Rahul": [1, 1]}]
        value.add_students("Nikhil", [2, 3])
        value.add_students("Rahul", [1, 1])


        #act
        answer=value.cal_grade()
        #assert
        self.assertEqual(answer,[5,2])

    def test_add_students_to_file(self):
        value=StudentExample(2)
        #value.students=[{"Mkin": [2, 3]},
         #               {"Josh": [1, 1]}]
        value.add_students("Nikhil", [2, 3])
        value.add_students("Rahul", [1, 1])

        path = value.add_students_to_file()

        #assert : so our goal here is to check if the content is added to the file or not so that what we are checking here..
        with open(path, "r") as file:
            content = file.read()

        self.assertEqual(content, str(value._students))


    def test_calcualte_marks(self):

        answer=StudentExample.cal_marks([2,4,3])
        #assert
        self.assertEqual(answer,9)


if __name__ == '__main__':
    unittest.main()
