"""
how iterator works and how you can build your own
iterator using __iter__ and __next__ methods.

Iterator in Python is simply an object that CAN BE iterated upon.
An object which will return data, one element at a time.

Technically speaking, Python iterator object must implement two special methods,
        __iter__()
and
        __next__(),
 collectively called the iterator protocol.

An object is called ITERABLe if we can GET AN ITERATOR from it.
Most of built-in containers in Python like: list, tuple, string etc. are iterables.
"""

"""
next() function to MANUALLY ITERATE through all the items of an iterator
"""

# define a list
my_list = [4, 7, 0, 3]

# get an iterator using iter()
my_iter = iter(my_list)
#prints 4
# print(next(my_iter))
#
# #prints 7
# print(my_iter.__next__())
# print(my_iter.__next__())
# print(my_iter.__next__())
# print(my_iter.__next__())


"""
How for loop actually works?

Is actually implemented as.
"""

# create an iterator object from that iterable
iterable = [4, 7, 0, 3]
iter_obj = iter(iterable)

print('123')

# infinite loop
# while True:
#     try:
#         # get the next item
#         # element = next(iter_obj)
#         pass
#         # do something with element
#     except StopIteration:
#         # if StopIteration is raised, break from loop
#         break
"""So internally, the for loop creates an iterator object,
    iter_obj by calling iter() on the iterable.
Ironically, this for loop is actually an infinite while loop.
"""


"""The __iter__() method returns the iterator object itself.
If required, some initialization can be performed.

The __next__() method must return the next item in the sequence
"""

class PowTwo:

    def __init__(self,max = 0):
        self.max =max

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= self.max:
            result = 2**self.n
            self.n +=1
            return result
        else:
            raise StopIteration

a = PowTwo(4)
print(a.__next__()

# ??????????)
