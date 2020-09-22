import sys

def is_palindrome(n):
    """Check if an integer is a palindrome."""
    word_n = str(n)
    if len(word_n) <= 1:
        return True
    else:
        first, last = word_n[0], word_n[-1]
        return (first == last) and (is_palindrome(word_n[1:-1]))

def solution(num_digits):
    start = 10 ** (num_digits - 1)
    stop  = (10 ** num_digits)
    palindromes = [(x, y, x * y) for x in range(start, stop) \
                                 for y in range(start, x + 1) \
                                 if is_palindrome(x * y)]
    return max(palindromes, key = lambda t: t[2])

if __name__ == '__main__':
    n = int(sys.argv[1])
    print(solution(n))
