import os
import shutil

"""
So we have modules like random for the random numbers, math for math calculations, os for the files/folders ,
shutil for the copy/move files and then datetime for the dates/time
os = check/create/delete/rename files and folders
shutil = copy/move files and folders
"""
print("_______________________")
print(os.getcwd())
print(os.listdir())

if os.path.exists("marks.txt"):
    print("the path is there")
else:
    print("the path is not there")

try:

    os.mkdir('hoep')
except:
    print("path is there")

folder = "backup"
file_name = "notes.txt"
# Because different systems use paths differently:
path = os.path.join(folder, file_name)

print(path)

"""
This program:

Creates a folder called backup
Creates a file called notes.txt
Writes something into it
Copies it into backup
"""

folder="hide"

if not os.path.exists(folder):
    os.mkdir(folder)

with open('textbook.txt','w') as f:
    f.write("helo is this my firle")

shutil.copy('textbook.txt',folder)
print("file copied")
os.listdir()



