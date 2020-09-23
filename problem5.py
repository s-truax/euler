from itertools import count

def first_true(pred, iterable, default=None):
    """Reference:
         https://docs.python.org/3/library/itertools.html#itertools-recipes"""
    return next(filter(pred, iterable), default)

def largest_factor(n):
    """Find the largest factor of N that is greater than 1 and less than N.

    In the case where N is prime, return N.
    """
    stop = int(n ** 0.5) + 1  # int takes only the integer part of a float
    smallest = first_true(lambda i: n % i == 0, range(2, stop), 1)
    return n // smallest

def prime_factorize(n):
    """Find the prime factorization of N."""
    return

def sequentially_divisible(m, n):
    """Assert that m is divisible by all positive integers up to and
       including n."""
    return n <= m and all([m % i == 0 for i in range(1, n + 1)])

def bf_solution(n):
    """Find the smallest integer divisible by all positive integers
       up to n."""
    positive_ints = count(1)
    return first_true(lambda i: sequentially_divisible(i, n), positive_ints)
    
    
    
