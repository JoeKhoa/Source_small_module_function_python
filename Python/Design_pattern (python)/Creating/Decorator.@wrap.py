"""     PROBLEM WITH NO - @wraper
Basically what is happening here is that the decorator is changing
the decorated function’s name and docstring to its own.
"""



from functools import wraps
def logged(func):
    # @wraps(func)
    def with_logging(*args, **kwargs):
        """with_logging-Doc: does some inner decorator"""
        print(func.__name__ + " was called")
        return func(*args, **kwargs)
    return with_logging

@logged
def f(x):
   """f-Doc: does some math"""
   return 'Origin-f: '+str(x + x * x)
print(f(2))
print('\n')
print(f.__name__)  # prints 'f' keep the origin of f
print(f.__doc__)   # prints 'does some math'
print(dir(logged))

"""

NO @wrap    =>      with_logging    changed by decorator return
                    None
"""
