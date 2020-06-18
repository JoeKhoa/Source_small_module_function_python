
import pprint


payload = {'abc': 'test@gmail.com',
            'password': 'testpass'
        }

print(*payload)
# abc password

def print_dict(**kwargs):
    print(kwargs)

print_dict(x=1,y=2,z=3)

def print_dict(*kwarg):
    print(kwarg)

print_dict('A','1', 2)
