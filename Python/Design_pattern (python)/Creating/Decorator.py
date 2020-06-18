def  make_tag(tag_name):
    def deco(f):
        def wrapper(x):
            x+='.'
            return "<%(tag)s>%(text)s</%(tag)s>" % dict(tag = tag_name, text = f(x) )
        return wrapper
    return deco

def tobe_decorated(x):
    return 'abc'

if __name__ == '__main__':
    tobe_decorated = make_tag('div')( make_tag('div')( make_tag('a')(tobe_decorated) ))
    print(tobe_decorated.__name__)
    print(tobe_decorated(' this will be decorated by tags! '))





from functools import wraps

def make_blink(func):
    """Define the decorator """

    # this make decorator transparent in term of its name and docstring
    #   Define the inner function
    @wraps(func)
    def decorator():
        # Grab the return value of the function being decorated
        re = func()
        tag = 'a'
        return "<"+tag+">" +re+ "</"+tag+">"
    return  decorator

#   Apply the decorator here
# @make_blink
@make_blink
def hello_world():
    return  " hello_world "

# print(hello_world())
# print(hello_world.__name__)
# print(hello_world.__doc__)
# print(dir(hello_world))


"""In order to understand about decorators, we must first know a few basic things in Python.

We must be comfortable with the fact that,
everything in Python (Yes! Even classes), are objects.
Names that we define are simply identifiers bound to these objects.
Functions are no exceptions, they are objects too (with attributes).
Various different names can be bound to the same function object.
"""

def first(msg):
    print(msg)

# first("Hello")
# second = first  #   the names first and second refer to the same FUNCTION OBJECT.
# second("Hello")


def inc(x):
    return x + 1

def dec(x):
    return x - 1

#    functions as arguments are also called higher order functions
def operate(func, x):
    result = func(x)
    return result

x = operate(inc,3)
y = operate(dec,3)
# print(dir(x) )
# print(x)
# print(y)



"""Furthermore, a function can return another function."""
def is_called(a):
    print("Outer a = ",a)
    def is_returned(x):
        print("inner x = ",x)
    return is_returned

# new = is_called(5)
#  new(x) = is_returned(x)
# new(1)  new(1)

"""Functions and methods are called callable as they can be called.
In fact, any object which implements the special method __call__() is termed callable.
So, in the most basic sense, a decorator is a callable that returns a callable.

Basically, a decorator TAKES IN A FUNCTION, ADDS some FUNCTIONALITY and RETURNS it.
"""
"""In the example shown below, make_pretty() is a decorator. In the assignment step.
"""

def make_pretty(func):
    def inner():
        print("I got a decorated ")
        func() # or return func
    return inner

def ordinary():
    print("I am ordinary")
# pretty = make_pretty(ordinary)()  # = return inner

# pretty = make_pretty(ordinary)
# print('my real function-name is :',pretty.__name__)
# pretty()


"""The function ordinary() got DECORATED or be decorated ( acctually it is made pretty )
 and the returned function was given the name pretty => pretty = inner .
"""

"""       MAIN CONCEPT
We can see that the decorator function ADDED SOME NEW FUNCTIONALITY TO THE ORIGIN FUNCTION.
This is similar to PACKING A GIFT. The decorator acts as a WRAPPER.
The NATURE of the object that got DECORATED (actual gift inside) does NOT ALTER
But now, it looks pretty (since it got decorated).
"""

"""        CRUCIFIED CONCEPT OF @symbol
Generally, we decorate a function and reassign it as,

We can use the @ symbol along with the name of the decorator function
and place it above the definition of the function to be decorated.
Generally, we decorate a function and reassign it as,
ordinary = make_pretty(ordinary)
"""

#   ***************************************************************************************

#   This is a common construct and for this reason, Python has a syntax to simplify this.
# @make_pretty
# @make_pretty
# @make_pretty
# @make_pretty
# def ordinary():
#     print("I am ordinary")
# ordinary()

""" _________________ is equivalent to => ..................... """

# def ordinary():
#     print("I am ordinary")
#  #   hard to know
# ordinary = make_pretty(
#                 make_pretty(
#                     make_pretty(
#                         make_pretty(ordinary)
#                                 )
#                             )
#                         )
#
# ordinary()
#  ************************************************************************************************


"""demo example"""
def smart_divide(func):
    def inner(a,b,c):
        print("I'm inner_son_of_decorate, divide",a,'and',b)
        if b == 0:
            print('whoops! cannot devide')
            return
        return func(a,b)
    return inner

@smart_divide
def divide(a,b,c=5):
    return a/b

# divide = smart_divide(divide)
# print(divide(1,2,3))



# ********* GOOD EXAMPLE


def works_for_all(func):
    def inner(*args, **kwargs):
        print("I can decorate any function")
        return func(*args, **kwargs)
    return inner




def star(func):
    def inner(*args, **kwargs):
        print("*" * 30)
        func(*args, **kwargs)
        print("*" * 30)
    return inner

def percent(func):
    def inner(*args, **kwargs):
        print("%" * 30)
        func(*args, **kwargs)
        print("%" * 30)
    return inner

# @star
# @percent
def printer(msg):
    print(msg)
# printer("Hello")
#
# printer = star(percent(printer))
# printer('Hi all')
