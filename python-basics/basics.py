from util import header

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

# The commented part doesn't work as they have different types.
# print(name + 12)
print(name + str(12))

# But dynamic, we can change the runtime type of a variable
# by assigning it a new value
name = float(21)
name = "Mate"

header("Functions")
# Python scopes are defined by indentation
def hello(who):
    print("Hello {}!".format(who))

hello(name)

# Python has builtin functions
# https://docs.python.org/3.4/library/functions.html
# len is a builtin function to get length
print(len("This is a long sentence!"))
# input evaluates python expression in 2.7, not in 3+
# As a result, with 2.7 you have to write "Mate" with 
# 3, Mate is enough, without quote marks.
s = input("Your name: ")
hello(s)


# Python has named parameters, parameters can be referenced by
# name
hello(who = "BME")

def hello_with_defaults(name, greet="Hello"):
    print("{} {}!".format(name, greet))

hello_with_defaults("Mate")
hello_with_defaults("Mate", greet="Good morning")
# This doesn't work because positional parameters has to be first,
# named parameters have to folllow them.
# hello_with_defaults(greet="Good morning", "Mate")

def multiple_return():
    return "BME", "Egyetem"

bme, category = multiple_return()
print(bme)
print(category)

# Multiple values can be used to swap variables.
first = "first"
second = "second"
print(first, second)
first, second = second, first
print(first, second)



# Function's can be values
def greet(hello):
    hello("Greetings")

# Control flow
header("Control flow")

# if
# Instead of brackets ({,}) python uses :
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

# To use index, use the enumerate builtin function
for i,name in enumerate(["Mate", "Steve", "Chris", "Angelica"]):
    print("{}: {}".format(i, name))
