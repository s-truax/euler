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

def is_prime(n):
    return largest_factor(n) == n

def add_dictionaries(d1, d2):
    """Make a new {Any -> int} dictionary using the union of the keys from
       d1 and d2 and summing the values for identical keys.

    >>> a = {'one': 1, 'two': 2, 'three': 3}
    >>> b = {'one': 1, 'two': 20, 'ten': 10}
    >>> add_dictionaries(a, b)
    {'one': 2, 'two': 22, 'three': 3, 'ten': 10}
    """
    keys_union = d1.keys() | d2.keys()
    return {k: d1.get(k, 0) + d2.get(k, 0) for k in keys_union}

def prime_factorize(n):
    """Find the prime factorization of N."""
    if is_prime(n):
        return {n: 1}
    one_factor = largest_factor(n)
    left_factors = prime_factorize(n // one_factor)
    right_factors = prime_factorize(one_factor)
    return add_dictionaries(left_factors, right_factors)

def solution_helper(n):
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
    
    
    
