from math import ceil

def is_factor(a, b):
    """Check if a is a factor of b."""
    q, r = divmod(b, a)
    return not r

def largest_factor(n):
    """Find the largest factor of N that is not N, unless N is prime."""
    stop = ceil(n ** 0.5)
    for i in range(2, stop):
        q, r = divmod(n, i)
        if r == 0:
            return q
    return n 

def solution(n):
    """Could be done recursively, but I fear stack overflows."""
    curr = n
    next = largest_factor(curr)
    while curr != next:
        curr, next = next, largest_factor(next)
    return curr

if __name__ == '__main__':
    import sys
    n = int(sys.argv[1])
    print(solution(n))
