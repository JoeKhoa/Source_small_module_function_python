"""The use of nonlocal keyword is 'very much similar to the global keyword'.
nonlocal is used to declare that a variable inside a nested function
is not local to it, meaning it lies in the OUTER INCLOSING function.
If we need to modify the value of a non-local variable inside a nested function,
then we must declare it with nonlocal.
Otherwise a local variable with that name is created inside the nested function.
"""


def outer_function():
    a = 5
    print("Initiate a :",a)
    def inner_function():
        nonlocal a
        a = 10
        print("Inner function a :",a)
    inner_function()
    print("Outer function a :",a)
outer_function()


globalVar = 10
def read1():
    print('globalVar : ' + str(globalVar) )

def write1():
    global globalVar
    globalVar = 5

def write2():
    globalVar = 15

# read1()
# write1()
# read1()
# write2()
# read1()
