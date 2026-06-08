"""


Practice Questions: Dictionaries

Try these yourself.

Practice 1

Create a dictionary called student with:

name
age
marks
city

Print each value.
"""
from collections import defaultdict

dict={"name":"nikhil", "age":12, "marks":45, "city":"guntur"}

"""
Practice 2
Update the marks in the dictionary.
Example:
marks: 90 -> 95
"""

dict["marks"]=95
print(dict)

"""
Practice 3
Add a new key:
grade
"""
dict["grade"]=5
print(dict)

"""
Practice 4
Remove the city key.
"""
del dict["city"]
print(dict)


"""
Practice 5
Use .get() to access a key that exists and a key that does not exist.
"""
print(dict.get("city"))
print(dict.get("grade"))

"""
Practice 6

Loop through the dictionary and print:

key -> value
"""

for a in dict:
    print(f'{a} : {dict[a]}')


"""
Practice 7
Given:
marks = {
    "Math": 90,
    "Science": 85,
    "English": 75
}

Calculate total marks.
"""

marks = {
    "Math": 90,
    "Science": 85,
    "English": 75
}

sum=0
for a in marks:
    sum=sum+marks[a]
print(sum)


"""
Practice 8
Given:
words = ["apple", "banana", "apple", "orange", "banana", "apple"]
Count frequency of each word using a normal dictionary.
"""

words = ["apple", "banana", "apple", "orange", "banana", "apple"]
dict_words={}
for a in words:
    if a in dict_words:
        dict_words[a]+=1
    else:
        dict_words[a]=1
print(dict_words)

"""
Practice 9
Do the same word count using defaultdict(int).
"""
from collections import defaultdict

defat_words=defaultdict(int)
print(defat_words)
for a in words:
    defat_words[a]+=1

print(defat_words)




"""
Practice 10

Given:

employees = [
    {"name": "Nikhil", "salary": 90000, "department": "Engineering"},
    {"name": "Madhu", "salary": 80000, "department": "HR"},
    {"name": "Akhil", "salary": 95000, "department": "Engineering"}
]

Print only employees from "Engineering".
"""
employees = [
    {"name": "Nikhil", "salary": 90000, "department": "Engineering"},
    {"name": "Madhu", "salary": 80000, "department": "HR"},
    {"name": "Akhil", "salary": 95000, "department": "Engineering"}
]
for a in employees:
    if a["department"]=="Engineering":
        print(a["name"])



"""
Practice 11
Sort the employees by salary from low to high.
"""
#employees.sort('salary')

employees.sort(key=lambda emp: emp["salary"])
print(employees)

print(employees)


"""
Practice 12
Group employees by department using defaultdict(list).

"""

