"""
Nonlocal variable in a nested function
Before getting into what a closure is, we have to first understand
what a nested function and nonlocal variable is.

A function defined inside another function is called a nested function.
Nested functions can access variables of the ENCLOSING scope.

In Python, these non-local variables are READ ONLY by default
and we must declare them explicitly as non-local (using NONLOCAL keyword)
in order to modify them.

 """

def outer_print_msg(msg):   # msg is NONLOCAL
 # This is the outer enclosing function
    def inner_printer():
         # This is the nested function
         print(msg)
    inner_printer()

# outer_print_msg(' Hello world! ')

""" -> We can see that the nested function printer() was ABLE TO ACCESS
the non-local variable msg of the enclosing function. => NOT CLOSURE """

#   Defining a Closure Function


def outer_print_msg(msg):   # msg is NONLOCAL
 # This is the outer enclosing function
    def inner_printer():
         # This is the nested function
         print(msg)
    return inner_printer

# another = outer_print_msg("Hello")
# another()   # why this_guy_another still know "Hello"
"""The outer_print_msg() function was called with the string "Hello" and
    the returned function was bound to the name "another".
On calling another(), the message was STILL REMEMBERED,
    ALTHOUGH we had ALREADY FINISHED EXECUTING the outer_print_msg() function.
This technique by which some data ("Hello") GETS ATTACHED to the code is called closure in Python.
"""
# del outer_print_msg
# another()
# try :
#     outer_print_msg('Hello')
# except :
#     print ("function : outer_print_msg() is deleted " )

"""This value in the enclosing scope is remembered even when
the variable goes out of scope or the function itself is removed from the current namespace."""


"""
When do we have a closure?

     have a nested function
     The nested function must refer to a value defined in the enclosing function.
     enclosing function must return the nested function.
"""

"""When to use closures?
So what are closures good for?

Closures can avoid the use of global values and provides some form of data hiding.
It can also provide an object oriented solution to the problem.

When there are few methods (one method in most cases) to be implemented in a class,
closures can provide an alternate and more elegant solutions.
But when the number of attributes and methods get larger, better implement a class."""


def make_multiplier_of(n):  # n is remembered!!!
    def multiplier(x):
        # nonlocal n
        # n+=1
        return x * n        #  is nochange => n is CONST in multiplier()
    return multiplier

# Multiplier of 3
times3 = make_multiplier_of(3)
# print('now, name of real_name_of_times is ->',times3.__name__)
# print( times3(3) )
# # Multiplier of 5
times5 = make_multiplier_of(5)


# # Output: 27
print(times3(9))
#
# # Output: 15
print(times5(3))
#
# Output: 30
print(times5(times3(2)))
""" so Green """
print(dir(times3))
# print ( .__doc__)
print ( times3.__closure__)
print('times3.__closure__[0].cell_contents : ',times3.__closure__[0].cell_contents)
print('times5.__closure__[0].cell_contents : ',times5.__closure__[0].cell_contents)
