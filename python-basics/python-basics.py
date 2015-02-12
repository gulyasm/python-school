### Utility
def separator():
    print("-" * 20)

def header(section):
    print("")
    separator()
    print("=== {} ===".format(section))
    separator()

# How to run a python program
#   1. `python <file>`
#   2. python console
#   3. ipython

# =======================
# Basics
# ======================
print("Hello world!")

# Variables
header("Variables")
name = "Mate" 
print(name)

# Types:
# boolean
# integer
# long
# float
# string
# list
# object
# None

# Python is a typed language
type(name)

# This on doesn't work as they have different types.
#print(name + 12)
print(name + str(12))

# But dynamic, we can assign variables to different types.
name = float(21)
name = "Mate"

header("Functions")
# Python scopes are defined by indentation
def hello(who):
    print("Hello {}!".format(who))

hello(name)

def hello_with_default(who="John Doe"):
    print("Hello {}!".format(who))

hello_with_default("BME")
hello_with_default()

def multiple_return():
    return "BME", "Egyetem"

bme, category = multiple_return()
print(bme)
print(category)

# Function's can be values
def greet(hello):
    hello("Greetings")

# Control flow
header("Control flow")
# if
def hello2(who):
    if len(who) > 4:
        print("Hello {}!".format(who))
    else:
        print("Too short name to greet! :( ")

# negate with not
def hello3(who):
    if not len(who) < 4:
        print("Hello {}!".format(who))
    else:
        print("Too short name to greet! :( ")


# None is the null type
if not None:
    print("Something went utterly wrong")

# for 
for i in range(5):
    print(i)

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
print(type(multiple_return()))

# To access a tuple element, use indexing
print t[0]

# Tuple is immutable, delete doesn't work
# del t[0]


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

