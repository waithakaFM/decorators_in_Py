# Decorators:
#   a decorator is a function
#   that takes another function and extends the behavior of that function
#   without explicitly modifying it.


#  create a function
# def my_function(arg):
#     """docstring"""
#     statement --> return a value
#
# my_function() --> calling a

def add_one(number):
    """A function that adds one to the number and then return the results"""
    return number + 1


print(add_one)
print(add_one(9))
print(add_one(99))

#  we can assign a variable to the add_one function
add_one_also = add_one
print(add_one_also)  # add_one_also is now the same as add_one
print(add_one_also(999))
print(add_one_also(9999), "\n")


#  the above shows that functions are first class objects


# create another function
def say_hello(name):
    return f"Hello {name}"


print(say_hello("franco"))


def be_amazing(name):
    return f"Yo {name}, you are amazing"


print(be_amazing("Mwas"))

myList = [say_hello, be_amazing]
print(myList[0])  # calls the say_hello function

print(myList[1]("Marie"))  # call the second function with the arguement


# a function that cam call another function
def greet_Bob(greeter_func):
    return greeter_func("Bob")


print(greet_Bob)
print(greet_Bob(say_hello))
print(greet_Bob(be_amazing))