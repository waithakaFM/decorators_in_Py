# Generators are functions that return an object that can be iterated over
# they generate the item inside the object easly one at a time only when you ask for it
# it is memory efficient in large data set

def my_generator():
    yield 2
    yield 4
    yield 3


g = my_generator()

# for i in g:
#     print(i)


# value = next(g) # execute the function until it reaches the first yield statement and return the value.
# print(value)
#
#
# value = next(g)  # run until the second yield statement and so on
# print(value)
#
#
# value = next(g)
# print(value)


# value = next(g)  # if I run it the 4th time it will raise an error of stop iteration
# print(value)

# use generator as input to other function to take in iterables

# print(sum(g))  # returns 6

print(sorted(g), '\n')  # return a list of all the object in sorted order


# look of execution of generator
def countdown(num):
    print('Starting')
    while num > 0:
        yield num
        num -= 1


cd = countdown(5)

value = next(cd)  # start from the beginning of the function and execute it
print(value)

print(next(cd))
print(next(cd))
print(next(cd))
print(next(cd))
