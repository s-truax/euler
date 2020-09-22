import sys

def is_palindrome(n):
    """Check if an integer is a palindrome."""
    word_n = str(n)
    if len(word_n) <= 1:
        return True
    else:
        first, last = word_n[0], word_n[-1]
        return (first == last) and (is_palindrome(word_n[1:-1]))

def digit_pairs_generator(num_digits):
    """Generates pairs of n digit numbers."""
    start = 10 ** (num_digits - 1)
    stop  = (10 ** num_digits)
    for x in range(start, stop):
        for y in range(start, x + 1):
            yield (x, y)
 
def lazy_solution(num_digits):
    def multiply_pair(ordered_pair):
        x, y = ordered_pair
        return x, y, x * y
    n_digit_pairs    = digit_pairs_generator(num_digits)
    n_digit_products = map(multiply_pair, n_digit_pairs)
    palindromes      = filter(lambda t: is_palindrome(t[2]), n_digit_products)
    return max(palindromes, key = lambda t: t[2])

if __name__ == '__main__':
    n = int(sys.argv[1])
    print(lazy_solution(n))
