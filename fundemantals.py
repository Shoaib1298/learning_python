
# * get input name and print

name = input("what is your name? ")
print("hello,",name)
print("hello, " + name)    ##intresting concatination of strings


list = [0,3,2,3]
list.pop(1)
print(list)
#try and expt function:
try :
    print("my name is :",sys.argv[1], ", and this is written in file :",sys.argv[0])
except IndexError:
    print("please write ur name")


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
