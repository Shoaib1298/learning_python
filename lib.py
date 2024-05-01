import random
import sys
import cowsay

# todo random.choice
# choin = random.choice(["up", "down"])

# print(choin)

# num = random.randint(1, 10)

# print(num)

# todo random.shuffle

# fruits = ["apple","banana","orange"]

# random.shuffle(fruits)

# print(fruits)

# print("my name is :",sys.argv[1], ", and this is written in file :",sys.argv[0])


#! learning try

# try :
#     print("my name is :",sys.argv[1], ", and this is written in file :",sys.argv[0])
# except IndexError:
#     print("please write ur name")

# if len(sys.argv) < 2:
#     sys.exit("too few arg")
# if len(sys.argv) > 2:
#     sys.exit("too many arg")

# print("my name is :",sys.argv[1], ", and this is written in file :",sys.argv[0])

# ? what is difference b/w list and array and vector

#! learning scaling an list

# if len(sys.argv) < 2:
#     sys.exit("too few arg")

# for arg in sys.argv[1:] :

#     print("name of coder is :",arg)


# Better_comments

# ? why is this true
# ! wait a ,something is wrong
# //my name is khan
# *apple
# todo banana

#! arr[-1] mean last element but the notation differs in slicing

# apple = [1,2,3,4]
# print(apple[0:-1])

# todo cowsay

if len(sys.argv) == 2:
    cowsay.cow("hellow," + sys.argv[1])

#! note the concatination of strings +


# * not important for now

# import requests
# import json

# if len(sys.argv)!=2:
#     sys.exit()

# result = requests.get("https://http//itunes.apple.com/search?entity=song&limit=50&term=weezer")
# o = result.jason()
# #! to understand this i need to have a clear understanding of Dic
# for result in o["results"]:
#     print(result["trackName"])

#!   most intresting

# def main():
#     print("apple")

# if __name__ == "__main__":
#     main()

# todo style: use black python reformatter
