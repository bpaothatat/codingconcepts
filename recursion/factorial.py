def factorial(n:int) -> int:
    if not isinstance(n, int): raise TypeError('Expected an integer')
    if n == 0: return 1
    return n * factorial(n - 1)
