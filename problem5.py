from functools import reduce
from itertools import count
from operator import mul

def first_true(pred, iterable, default=None):
    """Get the first element in an iterable that satisfies a predicate.

    If no element satisfies the predicate, return default.
    
    Reference:
         https://docs.python.org/3/library/itertools.html#itertools-recipes
    """
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
       d1 and d2 and summing the values corresponding to identical keys.

    >>> a = {'one': 1, 'two': 2, 'three': 3}
    >>> b = {'one': 1, 'two': 20, 'ten': 10}
    >>> add_dictionaries(a, b)
    {'one': 2, 'two': 22, 'three': 3, 'ten': 10}
    """
    keys_union = d1.keys() | d2.keys()
    return {k: d1.get(k, 0) + d2.get(k, 0) for k in keys_union}
   
def maximize_dictionaries(d1, d2):
    """Make a new {Any -> int} dictionary using the union of the keys
       from d1 and d2 and taking the max of the values with identical keys.
    
    >>> a = {'one': 1, 'two': 2, 'three': 3}
    >>> b = {'one': 1, 'two': 20, 'ten': 10}
    >>> add_dictionaries(a, b)
    {'one':1, 'two': 20, 'three': 3, 'ten': 10}
    """
    keys_union = d1.keys() | d2.keys()
    return {k: max(d1.get(k, 0), d2.get(k, 0)) for k in keys_union}

def prime_factorize(n):
    """Find the prime factorization of N.

    The prime factorization of a number N is represented as an {int -> int}
    dictionary, where the keys are prime numbers in the factorization of N
    and the value assoicated with each key is the power for that prime in
    the factorization of N.

    >>> prime_factorize(18)
    {1: 1, 2: 1, 3:2}
    >>> prime factorize(5)
    {5: 1}
    """
    if is_prime(n):
        return {n: 1}
    one_factor = largest_factor(n)
    left_factors = prime_factorize(n // one_factor)
    right_factors = prime_factorize(one_factor)
    return add_dictionaries(left_factors, right_factors)

def solution_helper(n):
    """Give the prime factorization for the solution for numbers
       up to N."""
    if n == 1:
        return {1: 1} 
    n_factors = prime_factorize(n)
    prev_factorization = solution_helper(n - 1)
    return maximize_dictionaries(n_factors, prev_factorization)

def solution(n):
    solution_factorization = solution_helper(n)
    prime_powers_factorization = {pow(p, e) for p, e in
                                  solution_factorization.items()}
    return reduce(mul, prime_powers_factorization, 1)

def sequentially_divisible(m, n):
    """Assert that m is divisible by all positive integers up to and
       including n."""
    return n <= m and all([m % i == 0 for i in range(1, n + 1)])

def bf_solution(n):
    """Find the smallest integer divisible by all positive integers
       up to n.

    Brute-force solution.
    """
    positive_ints = count(1)
    return first_true(lambda i: sequentially_divisible(i, n), positive_ints)

"""
TODO:
1. [ ] Read up on prime factorization algorithms.
2. [ ] Read about the complexity of multiplication, division, addition.
3. [ ] Read about primality testing.
4. [ ] Prove that this solution is correct?
5. [ ] Write a general `union_dicts` function.
6. [ ] Memoize functions?
"""
