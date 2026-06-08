#Container Data Types

"""
List: storing obj in sequence, dynamic(grow and shring in size),Mutable, random access by indeex.
Dictionaris: Key value pairs
Tuples: ordered collection. but immutable
Set: collection of unique items. its unordered..


"""


empty_list=[]
print(empty_list)
books=["abc","def", "Height","def"]
print(books)
print(books[0])
print(books[2])
print(books[-1])
print(len(books))
books.append(1)
print(books)
books.insert(0,"Super")
print(books)
books.pop()
print(books,"after pop")
#pop vs del key word. So if we use the pop it would return the delted element..but for the del it wont work like that.
del books[0]
print(books)
books.pop(0)
print(books)
books.remove("def")
print(books)
books.clear()
notbooks=[1,2,3,3,3,4,4]
books.extend(notbooks) #we can do this to add the multiple elements to the end of the list.
print(books)
print(books.count(4))

#List Slicing

numbers=[1,2,3,4,5,6,7,8,9]

#Example with all 3 parameters: start, stop and step
# numbers[start index: stop index : step]

even_numbers=numbers[1:8:2]
print(even_numbers)

first_3=numbers[:3]
print(first_3)
print(numbers[3:])
print(numbers[0:4])

print(numbers[3:6])

# slicing with -ve indices

print(numbers[-4:])

# Creating of copy of a list

planets_2026 = ["mercury", "venus", "earth", "mars", "jupiter"]

planets_2027=planets_2026

print(planets_2027)
print(planets_2026)

planets_2026.pop()
print(planets_2026)

print(planets_2027)

planets_2027_copy= planets_2027.copy()
planets_2027.pop()
planets_2026.pop()
print(planets_2027_copy)
print(planets_2027)
print(planets_2026)

planets_2026_slice= planets_2026[:]

print(planets_2026_slice)

print(planets_2026.remove("venus"),planets_2026)

# List comprehensions

squares=[a ** 2 for a in range(1,11)]

squares_even = [a **  2 for a in range(10) if a %2 ==0]


print(squares, squares_even)

#membership testing

lists=[3,5,2,5,6,3,6,3,2]

lists.sort()
#lists.sort(reverse=True)

temps=[3,4,5,3,2,5,22,63,6]
# sorted would provided the neew sorted list w
tempss=sorted(temps)
print(tempss)
# reverse method to turn the list up side down
lists.reverse()
print(lists)
#list concatenation and repetition
ab=[1,2,3]
ba=[3,4,5]
print(ab+ba)
print(ab*3)

#nested lists

wor=["a", "c"]
wors=wor*5
print(",".join(wors))
# all and any function

print(min(wors), max(wors))
print(sum(ab))
#list unpacking

coordinates=[0.712776,-74.005938,2342,343]
la,*li,sia=coordinates
print(la,li,sia)


#lists - Use cases


#inventory management application


inventory=[
    {
        "id":1,
        "name":"raghu",
        "qunatity":4,
        "price":15
    },
    {
        "id":2,
        "name":"ahil",
        "qunatity":2,
        "price":11
    },
    {
        "id":3,
        "name":"mainw",
        "qunatity":11,
        "price":5
    }
]


def add_product(inventory,product):
    return inventory.append(product)

def remove_product(inventory, product):
    # this below one is wrong logic..cause..we are deleting useing the index..but we need to do by the product id

    #return inventory.remove(inventory[product-1])
    i=[]
    for a in inventory:
        #print(a)
        if a["id"]==product:
            pass
        else:
            i.append(a)
    inventory=i
    return inventory


new_i=   {
    "id":4,
    "name":"hopeins",
    "qunatity":11,
    "price":51
}
add_product(inventory,new_i )
remove_product(inventory,2)
# so here in the remvoe case it wont work..it would only work if i gave the inventory =remove_product(inventory,2)
#
print(inventory)





# list are offten used in the frame works.. like flask

"""from flask import request

@app.route("/login", methods["GET","POST"])

def login():
    if request.method=="POST":
        return do_the_login()
    else:
        return show_the_login_form()"""

"""import pandas as pd

data =[
    ["alice",30],
    ["alice",30],
    ["alice",30],
    ["alice",30]
]
df=pd.DataFrame(data,colums=["Name","Age"])
"""
print("___________________________________")
#Dictionaries

home_dep={"hope":654,"kind":214,"super":334,"duper":134,"king":341}

print(home_dep["hope"])
print(home_dep.get("hope"))
print(home_dep.get("home","notfoune"))
home_dep["home"]=342
print(home_dep.get("home"))

# to merge the two dict we can use the merge operator...

hike_dep={2:"aisdnf",3:"wimd"}
print(home_dep | hike_dep)
#del method to delete from the list..

del home_dep['home']
print(home_dep.get("home"))
#pop method: removing and returning a value from the provided key (useful for use cases where you need the value after removal)
home_dep.pop("hope")
# so here if i gave variable = home_dep.pop("hope") then the variable will get value of the remvoed key

print(home_dep)
popitems= home_dep.popitem() # removing and returning the last element (key and value) from the dictionary
print(popitems)

home_dep.clear()
print(home_dep)
home_deps={"hope":654,"kind":214,"super":334,"duper":134,"king":341}

for a in home_deps:
    print(home_deps[a])

# dictionary comprehension

squares_dict= {x: x for x in range(20) if x%2==0}
print(squares_dict)


# transforming a dictionary

org_dict={"a":1,"b":2,"c":3,"d":4}
inv_dict={val:key for key,val in org_dict.items()}
print(org_dict)
print(inv_dict)

import copy

orgi_dict={"name":"nikhli teja", "hobbies":["reading","travelling"]}

#shallow copy

shallow_copied_dict=orgi_dict.copy()

shallow_copied_dict['age']=30

#deep copy

deep_copied_dict=copy.deepcopy(shallow_copied_dict)

#modifying the copies

shallow_copied_dict["hobbies"].append("testing")
deep_copied_dict["hobbies"].append("swimming")

print(orgi_dict)
print(shallow_copied_dict)
print(deep_copied_dict)

value_a=orgi_dict.setdefault("a",33)
print(value_a)



# what is the return type for range.
# so what is range

for a in range(5):
    print(a)



