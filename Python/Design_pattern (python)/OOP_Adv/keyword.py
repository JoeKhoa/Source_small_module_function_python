"""    yield   """

"""yield is used inside a function like a return statement. But yield returns a generator.
Generator is an iterator that generates one item at a time.
 A large list of value will take up a lot of memory.
  Generators are useful in this situation as it generates only one
  value at a time instead of storing all the values in memory. e.g: """


"""will create a generator g which generates powers of
 2 up to the number two raised to the power 99.
 We can generate the numbers using the next() function as shown below."""

g = (2**x for x in range(100))

# for i in range(5):
#     a = next(g)
#     print('next-'+str(i+1)+' : '+ str(a))

# # 1
# next(g)
# # 2
# next(g)
# # 4
# next(g)
# # 8
# next(g)
# 16

"""And so on… This type of generator is returned by the yield statement from a function.
 Here is an example."""

def generator():
    for i in range(5):
        yield i*i #  == return i*i (    yield is return_of_next()   )

g = generator()
for i in g:
    print(i)
