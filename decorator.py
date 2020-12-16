def decorat(func):
    def _handler(arg):
        arg/=2
        print('Decorated:')
        return func(arg)
    return _handler 

def ff(a):
    return a-1 

def fff(a):
    return a*1

@decorat
def f(a):
    return a+1

print(ff(2), '\n')
print(f(3), '\n')
print(fff(4), '\n')