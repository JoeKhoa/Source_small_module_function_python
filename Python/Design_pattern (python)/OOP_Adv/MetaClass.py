"""
https://www.python-course.eu/python3_metaclasses.php
"""

"""
Abstract classes are classes that contain one or more abstract methods.
An abstract method is a method that is declared,
but contains NO IMPLEMENTATION.
Abstract classes CANNOT BE INSTATIATED,
and require subclasses to provide implementations for the abstract methods.

"""
class AbstractClass:

    def do_something(self):
        pass

class B(AbstractClass):
    pass

a = AbstractClass()
b = B()

print(AbstractClass.__name__)
"""If we start this program, we see that this is not an abstract class, because:

we can instantiate an instance from
we are not required to implement do_something in the class defintition of B
"""
