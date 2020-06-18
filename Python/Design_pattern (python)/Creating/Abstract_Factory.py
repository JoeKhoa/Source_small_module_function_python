class Dog:
    """ One of the objects to be returned """

    def __str__(self):
        return "Dog"

    def speaker(self):
        return 'woof'


class DogFactory:
    """Concrete Factory"""

    def get_pet(self):
        """ Returns a Dog object """
        return Dog()

    def get_food(self):
        """ Returns a Dog Food object """
        return "Dog Food"


class PetStore:
    """ PetStore house our Abstract Factory """

    def __init__(self,pet_factory):
        """ pet_factory is our Abstract Factory """
        self._pet_factory = pet_factory

    def show_pet(self):
        """ Utility method to display the details of the objects returned by the DogFactory """
        pet = self._pet_factory.get_pet()
        pet_food = self._pet_factory.get_food()

        print('Out pet is: {}!'.format(pet))
        print('the {} is hello by: {}'.format(pet,pet.speaker() ))
        print('the food of {} is: {}'.format(pet,pet_food  ))

# Creat a Concrete-factory
factory = DogFactory()
# Create a pet store housing our Abstract Factory
petStore = PetStore(factory)
# Invoke the utility method to show the detail of our pet
petStore.show_pet()
