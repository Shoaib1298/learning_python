list = ["shoaib", "sohail", "faizan", "faiz"]
dis = {
    "shoaib": "myself",
    "sohail": "brother",
    "faizan": "bada chutiya",
    "faiz": "chutiya",
}


"""
there are two additional ways of using for loop
    -for x in list:
    -[x**2 for x in list]
    -'_' if the x is not is not necessary inside the loop
list have len and np.array have .shape {note the lack of ()}

"""
for name in dis:
    print(name, dis[name], sep=",")

l = [name for name in dis]
#! this for loop accesed keys as name

print(l)

list_dis = [
    {"name": "shoaib", "uni": "srmap", "age": 24},
    {"name": "sohail", "uni": "iiser", "age": 18},
]

for name in list_dis:
    print(name["name"], name["uni"], name["age"], sep=",")
#! this for loop accessed an entire dis as name
