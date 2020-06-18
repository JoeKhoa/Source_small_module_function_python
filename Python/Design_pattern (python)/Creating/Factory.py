class Dog:
    """ just an simple Dog class """
    def __init__(self,name):
        self.name = name

    def speaker(self):
        return 'woof'

class Cat:

    def __init__(self,name):
        self.name = name

    def speaker(self):
        return 'Meow'

def get_pet(pet = "dog"):

    """ *** the factory method *** """
    pets = dict(dog = Dog('A'), cat = Cat('B'))
    # pets = {'dog':Dog('A'), 'cat':Cat('B')}
    return pets[pet]    # just return an dict OBJECT_items like dog or cat

d = get_pet('dog')
print(d.speaker())
c = get_pet('cat')
print(c.speaker())
