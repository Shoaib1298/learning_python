import csv

"""

we can both read from a file and stores/write to a file.
-file = open("name_of_the_file","option")
 -options are :
  -"w" ;errases everthing from file and writes new info.
  -"a" ;appends the file , note : try to creat a new line for next append for clarity
  -"r" ;by default and only allows u to read the file.
 -we will have to close the file by using file.close()

-with open("name_of_the_file","option") as file :
    ---------------
    ---------------
 -once the with statement closes the file closes automatically

-Reading a file:
lines = file.readlines()
    #reads all the lines and stores them in a list
and this list can be used as pleased 

for line in file:
   # line assume the value of a line in the file ittratively from line zero to --

.csv file = comma seperated values file




"""
name = input("name :")

# file = open("names.txt","a")

# # "a"== append ,"w" ==write

# file.write(f"{name}\n")

# file.close()

# * alternate way


# with open("names.txt","a") as file:
#     file.write(name)

name = []

with open("names.txt") as file:
    for line in file:
        name.append(line.rstrip())

potters = []

with open("harry_potter.csv") as file:
    read = csv.DictReader(file)
    #! u cant always read an object but can often use it.

    for reading in read:
        student = {"name": reading["name"], "school": reading["school"]}
        potters.append(student)


# we could have sorted the dis as well but not a wise approach
# we want to sort by students name
def get_name(student):
    return student["name"]


#! passing a function in the arg of another function
# new_potters = sorted(potters,key=get_name)
#! alernatively lambda is a anoumous function
new_potters = sorted(potters, key=lambda student: student["name"])
for potter in new_potters:
    print(f"{potter['name']} is in {potter['school']}")

with open("harry_potter.csv", "a") as file:
    write = csv.DictWriter(file, fieldnames=["name", "school"])
