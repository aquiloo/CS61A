def search(f):
    """return the smallest non-negative x for which f(x) is a true value """
    x = 0
    while True:
        if f(x):
            return x
        x += 1

def invert(g):
    """return a function h(y) that returns x such that g(x) == y"""
    # g = x^2, f = (g(x) == y)?True:False
    # f = (x^2 ==y)?True:False
    return lambda y :search(lambda x : g(x)==y)

# only effective when input can be sqrted
sqrt = invert(lambda x: x*x)
print(sqrt(15))
