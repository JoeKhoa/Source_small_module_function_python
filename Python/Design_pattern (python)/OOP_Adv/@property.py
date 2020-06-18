""" http://www.trytoprogram.com/python-programming/python-property/
    https://www.programiz.com/python-programming/property
"""
# import pprint
"""
We can see above that new methods get_temperature() and
 set_temperature() were defined and furthermore,
 temperature was replaced with _temperature.
 An underscore (_) at the beginning is used to denote private variables in Python.
"""
# class Celsius:
#     def __init__(self, temperature = 0):
#         self.temperature = temperature
#
#     def to_fahrenheit(self):
#         return (self.temperature * 1.8) + 32


""" MORE ENCAPSULATION"""


# class Celsius:
#     def __init__(self, temperature = 0):
#         self.set_temperature(temperature)
#
#     def to_fahrenheit(self):
#         return (self.get_temperature() * 1.8) + 32
#
#     # new update
#     def get_temperature(self):
#         return self._temperature
#
#     def set_temperature(self, value):
#         if value < -273:
#             raise ValueError("Temperature below -273 is not possible")
#         self._temperature = value

# c = Celsius(50)
# print(c.to_fahrenheit())
# err = Celsius(-274)
# try :
#     print(err.to_fahrenheit())
# except:
#     print('error')

"""                     IMPORTANCE
    Please note that private variables don't exist in Python.
    There are simply norms to be followed.
    The language itself don't apply any restrictions.

    The big problem with the above update is that,
    all the clients who implemented our previous class in their program
    have to modify their code from obj.temperature to obj.get_temperature()
    and all assignments like obj.temperature = val to obj.set_temperature(val).

    => All in all, our new update was not backward compatible.
    This is where property comes to rescue.
"""
#
# class Celsius:
#
#     def __init__(self, temperature = 0):
#         self.temperature = temperature
#
#     def to_fahrenheit(self):
#         return (self.temperature * 1.8) + 32
#
#     def get_temperature(self):
#         print("fn Getting value")
#         return self._temperature
#
#     def set_temperature(self, value):
#         if value < -273:
#             raise ValueError("Temperature below -273 is not possible")
#         print("fn Setting value")
#         self._temperature = value
#
#     # temperature = property(set_temperature,get_temperature)   # This NOT WORK, It 's concern ORDER
#     temperature = property(get_temperature,set_temperature)


# #   fn Setting value
# c = Celsius(5)
#
# #   fn Getting value
# print(c.temperature)
# print ( c._temperature.__doc__)


# print(c.to_fahrenheit())


"""Any code that RETRIEVES the value of temperature will AUTOMACTICALLY call get_temperature()
instead of a dictionary (__dict__) look-up.
Similarly, any code that ASSIGNS a value to temperature will automatically call set_temperature()
. This is one cool feature in Python.
"""


"""
By using property, we can see that, we MODIFIED our class and
IMPLEMENTED the value constraint WITHOUT ANY CHANGE REQUIRED to the client code.
Thus our implementation was backward compatible and everybody is happy.

Finally note that, the actual temperature value is
stored in the PRIVATE variable _temperature. ( PRIVATE = belong to a Method)
The attribute temperature is a property object
which provides INTERFACE TO this private variable.
"""



"""
property(fget=None, fset=None, fdel=None, doc=None)
where, fget is function to get value of the attribute,
     fset is function to set value of the attribute,
     fdel is function to delete the attribute and doc is a string (like a comment).
     As seen from the implementation, these function arguments are optional.
     So, a property object can simply be created as follows.
 """

 # make empty property
# temperature = property()
# print(property.__doc__)
# print(c.temperature)
# assign fget
# temperature = temperature.getter(get_temperature)
# # assign fset
# temperature = temperature.setter(set_temperature)



class Celsius:
    def __init__(self, temperature = 0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    @property
    def temperature(self):  #   def temperature = x = variable
        print("Getting value")
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        if value < -273:
            # raise ValueError("Temperature below -273 is not possible")
            value = -273
        print("Setting value")
        self._temperature = value


c = Celsius(-1000)  #  use setting val
print(c.to_fahrenheit())
  # Setting value

print(c.temperature)
# print(c.to_fahrenheit())






# ****************************** OFFICIAL ******************************

"""
Property attribute.

  fget
    function to be used for getting an attribute value
  fset
    function to be used for setting an attribute value
  fdel
    function to be used for del'ing an attribute
  doc
    docstring

Typical use is to define a managed attribute x:

"""
# class C(object):
#     def getx(self): return self._x
#     def setx(self, value): self._x = value
#     def delx(self): del self._x
#     x = property(getx, setx, delx, "I'm the 'x' property.")

"""Decorators make defining new properties or modifying existing ones easy:
"""
class C(object):
    @property
    def x(self):
        "I am the 'x' property."
        return self._x
    @x.setter
    def x(self, value):
        print('do function setter')
        self._x = value
    @x.deleter
    def x(self):
        del self._x
