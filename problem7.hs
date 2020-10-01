{-|
  An implementation of the Sieve of Eratosthenes that uses
  list comprehension (i.e. filtering) to do the bulk of the work.

  Finds all primes less than or equal to N.
-}
filterSieve :: Int -> [Int]
filterSieve n = let
    doesNotDivide x y  = y `mod` x /= 0
    sift []            = []
    sift (p:xs)        =
        let sifted = [m | m <- xs, p `doesNotDivide` m]
        in if 2 * p >= n 
            then [p]
                else p : sift sifted
    in sift [2..n]

{-|
  Solution to Project Euler question 7 that uses the Sieve of Eratosthenes
  implemented by list comprehension / filtering.
-}
filterSolution :: Int -> Int
filterSolution = head . reverse . filterSieve

