"""
Write a script that takes user input and prints whether a number is odd or even.
"""
from lib2to3.fixes.fix_input import context

num=int(input("Enter the number to check if its even or odd: "))


if num%2==0:
    print("The entered number is Even")
else:
    print("The number is Odd")

"""
Write a function that returns the factorial of a number using a loop.
"""
try:
    fact=int(input("Enter the number to find its factorial: "))
    c=1
    for a in range(fact,1,-1):
        c=c*a

    def rec(ab):
        if ab==1:
            return ab
        return ab * rec(ab-1)

    print("The factorial of the ",fact,"is: ",c)
    print("The factorial of the ",fact,"using rec is: ",rec(fact))
except:
    print("enter valid string")




"""
Write a script that reads a comma-separated string and prints each item on a new line.
"""
str="s,g,e,wl,win,df"
print(str.split(","))
li=str.split(",")
for i in li:
    print(i)


"""
Write a temperature converter (Celsius ↔️ Fahrenheit) with input validation.
"""

input4= input("enter the temperature type C or F: ")

def celtofah(c):
    return (c*1.8)+32
def fahtocel(f):
    return (f-32)/1.8
def askuser():
    return input("enter the temperature type C or F: ")

while True:
    if input4=="C" or input4=="c":
        print("The input4: ",input4)
        C=int(input("Enter your Celsius:"))
        print("Your Fahrenheit is: ",celtofah(C))
        if input("do you still want to continue? Y or N: ")=="Y":
            input4=askuser()
        else:
            print("Thank you have a nice day")
            break
    elif input4=="F" or input4=="f":
        print("The input4: ",input4)
        F=int(input("Enter your Fahrenheit: "))
        print("Your Celsius is: ", fahtocel(F))
        if input("do you still want to continue? Y or N: ")=="Y":
            askuser()
        else:
            print("Thank you have a nice day")
            break
    else:
        print("Can you make sure to enter either C or F")
        input4= input("Try to enter again: ")





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

student=int(input("Enter the number of the students:"))


list={}
for a in range(student):
    sname=input("enter student name:")
    subs=["Maths","Phy","Che"]
    smarks={}
    for b in range(3):
        try:
            smarks[subs[b]]=float(input(f'enter marks in {subs[b]}'))
        except:
            print("enter valid marks")
    list[sname]=smarks
print(list)

def calgrade(values):
    print("The marks are:",values)
    return sum(values.values())
def calstopper(values):
    clstopper={}
    maxs=0
    topper=""
    for a in values:
        j=sum(values[a].values())
        clstopper[a]=j
        if j>maxs:
            maxs=j
            topper=a
    return topper,maxs

def addmarks():

    with open('marks.txt','w') as ma:
        #ma.write(str(list))
        a,b=calstopper(list)
        print("checking before..how list looks like: ", list)
        for val in list:
            ma.write(f'{val} : {list[val]} \n')
        ma.write(f'the class topper is: {a} with the marks of : {b}\n')




for a in list:
    print(f'The total marks for {a} are {calgrade(list[a])}')

def main():
    try:
        addmarks()
    except:
        print("there is no such file.")

main()







