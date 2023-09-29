import random

# Select a random item from a list
mylist = [1, 2, 3, 4, 5]
print(random.sample(mylist, 1))


# Select 3 random items from a tuple
mytuple = ('a', 'b', 'c', 'd', 'e')
print(random.sample(mytuple, 3))

# Select 2 random characters from a string
mystring = "hello"
print(random.sample(mystring, 2))