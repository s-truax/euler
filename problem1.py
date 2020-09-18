def solution(n):
    multiples_of_three = filter(lambda n: n % 3 == 0, range(n))
    multiples_of_five  = filter(lambda n: n % 5 == 0, range(n))
    multiples_of_15    = filter(lambda n: n % 15 == 0, range(n))
    return (sum(multiples_of_three) + sum(multiples_of_five) - 
             sum(multiples_of_15))

if __name__ == '__main__':
    import sys
    n = int(sys.argv[1])
    print(solution(n))    
