"""Python generators are a simple way of creating iterators.

Simply speaking, a generator is a function that RETURNS AN OBJECT (iterator)
which we can iterate over (ONE value at a time).

+   yield statement INSTEAD of a return statement
     Both yield and return will return some value from a function.

     The difference is that, while a return statement TERMINATES a function ENTIRELY,
     yield statement PAUSES the function saving all its states
     and later continues from there on successive calls.

"""
"""
     Differences between Generator function and a Normal function

        Generator function contains one or MORE yield statement.
        When called, it returns an object (iterator) but does NOT start execution IMMEDIATELY.
        Methods like __iter__() and __next__() are implemented automatically.
            So we can iterate through the items using next().
        Once the function yields, the function is paused
            and the control is transferred to the caller.
        Local variables and their states are REMEMEMBERED BETWEEN successive calls.
        Finally, when the function terminates,
            StopIteration is raised AUTOMATICALLY on further calls.

"""

    # A simple generator function
def my_gen():
    n = 1
    print('This is printed first')
    # Generator function contains yield statements
    yield n

    n += 1
    print('This is printed second')
    yield n

    n += 1
    print('This is printed at last')
    yield n

# my_gen() # this NOT WORKED
# a = my_gen()
# next(a)
# Once the function yields, the function is paused and the control is transferred to the caller.

# Local variables and theirs states are remembered between successive calls.
# next(a)
# next(a)
# Finally, when the function terminates, StopIteration is raised automatically on further calls.
# try :
#     next(a)
# except:
#     print( "StopIteration" )


"""
Python Generators with a Loop
"""

def rev_str(my_str):
    length = len(my_str)
    for i in range(length-1,-1,-1):
        yield   my_str[i]

# for char in rev_str('hello world'):
#     print(char, end ='_')
"""The major difference between a list comprehension and a generator expression is
that while list comprehension produces the ENTIRE list,
generator expression produces OME item at A TIME.

***  They are kind of LAZY, producing items ONLY WHEN ASKED FOR.
"""

my_list = [1, 3, 6, 10]

# square each term using list comprehension
# Output: [1, 9, 36, 100]
[x**2 for x in my_list]

# same thing can be done using generator expression
# Output: <generator object <genexpr> at 0x0000000002EBDAF8>
a = (x**2 for x in my_list) #   expression
# print( next(a) )
# print( next(a) )
# print( next(a) )

""" Great using way"""
# s =sum (x**2 for x in my_list)
# print('sum',s)
# m = max(x**2 for x in my_list)
# print('max',m)

def PowTwoGen(max  = 0):
    n = 0
    while max  < n :
        yield 2 ** n
        n=+1
a = next(PowTwoGen(3))
print(a)
