"""
this is also an comment
anything in between these trible cotes 

"""

# I am wondering if I should adapt writing sudo code as comments

# * get input name and print

# name = input("what is your name? ")
# print("hello,",name)
# print("hello, " + name)    ##intresting concatination of strings

# * pop removes i th element from the list and remove removes the first apperance of the arg in list

# list = [0,3,2,3]
# list.pop(1)
# print(list)

#! new and intresting

name = input("what is your name? ")

# ? I have hard time understanding when and when not to use ()

#! this is a method??- a built in function with a specific data type

name = name.strip()
name = name.title()
"""
if there is an data type it can be modified by data.fun()

"""

# * alternate way of doing this
# top to bottom, left to right

name = input("what is your name? ").strip().title()

print(f"hello, {name}")
