def fib(n):
    """Returns a list containing the Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    
    return result

def func(a, L=[]):
    L.append(a)
    return L