from util import header

# =======================
# Data structures
# ======================

# Dictionary
header("Dictionary")
d = {}
d["apple"] = "red"
d["banana"] = "yellow"

def color(fruit):
    if fruit in d:
        print("The {} is {}".format(fruit, d[fruit]))

color("banana")
color("kdsf")

del d["apple"]

# List
header("List")
l = []
l.append("Mate")
l.append(156)
l.append(1.1)
l.append({"apple": 12, "banana": 32})
# Fractal list :)
l.append(l)

# we can iterate over a list
# The way we can assign tuples to multiple values is called unzipping
for i,v in enumerate(l):
    print(i,v)

# Slicing
print(l[:2])
print(l[1:2])
print(l[2:])

# Containement test
if "Mate" in l:
    print("I'm in!")

# Delete from list
del l[2]    


# Tuples
header("Tuples")
t = ("Mate" * 2, 2)
print(t)

def multiple_return():
    return "BME", "University"

print(type(multiple_return()))

# To access a tuple element, use indexing
print t[0]

# Tuple is immutable, delete doesn't work
# del t[0]


# set
header("Set")
# To create a set:
a = set()
a.add("Mate")
print("Mate" in a)
print("Peter" in a)
print(len(a))
print("Mate" in a)
print("Mate" in a)
print("Mate" in a)
print(len(a))
a.add("Peter")
print(len(a))

# DEMO: Try out it the set operations in ipython
# https://docs.python.org/3.4/library/stdtypes.html#set

# =======================
# Classes
# ======================
header("Classes")
class Person():
    def __init__(self, name="John Doe"):
        self.name = name

    def greet(self, who):
        print("Hello {}, my name is {}!".format(who, self.name))

me = Person("Mate")
me.greet("You")


