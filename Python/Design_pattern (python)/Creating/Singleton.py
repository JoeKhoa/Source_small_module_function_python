
class Borg:
    """ Borg class make class Attributes Global """
    _share_state = {}   # Attributes Dict, can be others

    def __init__(self):
        self.__dict__ = self._share_state
class Singleton(Borg):  # Inherits from Borg class ClassName(object):
    """ This class now shares all Attributes among all its Instance """
    #   This is essential makes the Singleton Object and object-oriented Global variable

    def __init__(self, **dictArgs):
        # update the attributes dict by inserting a key pair value
        # print(dictArgs)
        self._share_state.update(dictArgs)

    def __str__(self):
        return str(self._share_state)

#       create Singleton object and add our first acronym
x = Singleton( HTTP = "Hyper Text Transfer Protocol")
#   print the object
print(x)

#   create another singleton and if it refers to the same attributes by adding another acronym
y = Singleton(SNMP = "Simple Network Management Protocol")
print(y)
