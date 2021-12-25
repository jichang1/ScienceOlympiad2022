"""
https://www.mikedane.com/programming-languages/python/getting-user-input/

https://stackoverflow.com/questions/19100730/making-a-greeting-program-in-python
"""

def greet(greeting):
    name = input("Hi, what's your name?\n") 

    if name.startswith("My name is "):
        name = name.replace("My name is ", "")
    elif name.startswith("my name is "):
        name = name.replace("my name is ", "")
    return greeting + name

print(greet("Hi, "))


"""
case one: modular
name = input("Enter your name: ")
print("Hello", name + "!")

case two: newline or not in the sample display

case three: handle user input, e.g. what if the user enters 
my name is Jane; 
My name is Jane
"""