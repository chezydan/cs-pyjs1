def mult (f):
    def wrapper(n):
        print( f(n)*2)
    return wrapper

@mult
def num(n):
    return n

num(4)