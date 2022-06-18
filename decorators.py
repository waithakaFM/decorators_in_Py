# function decorators- takes another function as an argument and extend the behavior of this function wthout
# explicitly modifying it.

# @myDecorator
# def doSomething():
#     pass

def start_end_decorator(func):
    def wrapper():
        print('Start')  # do something before
        func()
        print('End')  # do something after

    return wrapper


# def print_name():
#     print("Fabian")
#
#
# print_name = start_end_decorator(print_name) # when using decorators we no longer need this line
#
# print_name()

#  now we use the decorators
@start_end_decorator
def print_name():
    print("Fabian")


print_name()


# lets see what will happen is our function has some arguments
def start_end_decorator_with_args(func):
    def wrapper(*args, **kwargs):  # we can now use as many arguments as we can
        print('Start')  # do something before
        func(*args, **kwargs)
        print('End')  # do something after

    return wrapper


# @start_end_decorator
# def add_one(number):
#     return number + 1
#
#
# add_one(49)  # TypeError: wrapper() takes 0 positional arguments but 1 was given
#

# to fix the above error we need the same argument in our decorator func.
@start_end_decorator_with_args
def add_one(number):
    return number + 1


print(add_one(49), '\n')  # prints none


# to solve this we assign a variable to func and return it

def start_end_decorator_with_args(func):
    def wrapper(*args, **kwargs):  # we can now use as many arguments as we can
        print('Start')  # do something before
        results = func(*args, **kwargs)
        print('End')  # do something after
        return results

    return wrapper


@start_end_decorator_with_args
def add_one(number):
    return number + 1


results = add_one(999)
print(results)

# lets see the identity of this function
print(help(add_one))  # python got confused about the identity of the function
print(add_one.__name__, "\n")

# to correct the above mistake we import functools
import functools


def start_end_decorator_with_args(func):
    @functools.wraps(func)  # preserve info of my used function
    def wrapper(*args, **kwargs):  # we can now use as many arguments as we can
        print('Start')  # do something before
        results = func(*args, **kwargs)
        print('End')  # do something after
        return results

    return wrapper


@start_end_decorator_with_args
def add_one(number):
    return number + 1


print("The name of the function is: ", add_one.__name__)  # python now knows the function name

# the temperate for a nice decorator

# import functools
#
# def start_end_decorator_with_args(func):
#
#     @functools.wraps(func)  # preserve info of my used function
#     def wrapper(*args, **kwargs):  # we can now use as many arguments as we can
#         # do something before
#         results = func(*args, **kwargs)
#         # do something after
#         return results

#     return wrapper
