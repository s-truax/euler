from itertools import takewhile

def generate_fibs():
    curr, next = 1, 1
    while True:
        yield curr
        curr, next = next, curr + next

def solution(upper_bound):
    fibs          = generate_fibs()
    evens         = filter(lambda n: n % 2 == 0, fibs)
    bounded_evens = takewhile(lambda n: n <= upper_bound, evens)
    return sum(bounded_evens)

if __name__ == '__main__':
    import sys
    upper_bound = int(sys.argv[1])
    print(solution(upper_bound))
    
