# seq[start:end:step]
#
# So you can do:
def print_ls(ls):
    print('start = {}, stop = {}, step = {}'.format(ls.start,ls.stop,ls.step))
    for i in ls:
        print(i,end=' ')
    print('\n')
s = range(10)

x = range(100)[5:18:2]
# print(x.__doc__)
print_ls(x)
y = s[::3]
print_ls(y)
