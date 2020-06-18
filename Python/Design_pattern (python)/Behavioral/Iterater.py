
def count_to(count):    #   this use _"generator"_ return a_tuple
    # Our list
    number_in_german = ['eins','zwei','drei','vier','funf']

    # Build in iterator
    # create a tuple like : (1,'eins')
    iterator = zip(range(count),number_in_german)

    for position,number in iterator:
        #   return 'generator'-tuple containeing number in German
        yield number

# for number in count_to(3):
    # print("item : {}".format(number))


def iterator_ex():      #   returns us an iterator object- one value
    iter_obj = iter([3,4,5])
    print(next(iter_obj))
    print(next(iter_obj))
    print(next(iter_obj))
    # print(next(iter_obj)) # OVER-RANGE StopIteration


iterator_ex()
