class Subject:      #   what is being observered

    def __init__(self):
        self._observers = []    #   This were reference to all observers are being kept
                                #   Note that is one-many-relationship
                                #   one-object is observered by multiple observers
    def attach(self,observer):
        if observer not in self._observers:   # if observer is not already in the observer list
        # append observer to the list
            self._observers.append(observer)

    def detached(self,observer): #    simple remove the observer
        try :
            self._observers.remove(observer)
        except ValueError:
            pass

    def notify(self, modifier = None):
        for observer in self._observers:    #   For all observers in the list
            if modifier != observer:        #   Don't notify the observer who is actually updating the temperature
                observer.update(self)            #   Alert the observer


class Core(Subject):        #   Inherits from the Subject class

    def __init__(self, name = ""):
        Subject.__init__(self)
        self._name = name   #   set the name of the Core
        self._temp = 0      #   Initiate the name of the Core

    @property               #   Getter that get the temperature
    def temp(self):
        return self._temp

    @temp.setter            #   setter that set the core temperature
    def temp(self,temp):
        self._temp = temp
        #   notify the change when sb change the temperature


class TempViewer:

    def update(self,subject):  #    Alert method is invoked when the notify() method in a concrete subject is invoked
        print("TempViewer : {} has temperature {} ".format(subject._name,subject._temp) )

# Create subject
c1 = Core('Core 1')
c2 = Core('Core 2')

# Create observerTempViewer
v1 = TempViewer()
v2 = TempViewer()

# attach the observer to first core
c1.attach(v1)
c2.attach(v2)

# change temp of the first Core
c1.temp = 80
c2.temp = 90
