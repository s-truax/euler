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
        in p : sift sifted
    in sift [2..n]

-- Is there any way to add the square optimization to the above?

-- |Trial-division prime-checking function.
isPrimeTD :: Int -> Bool
isPrimeTD n
    | n <= 1    = False
    | otherwise = and [m `doesNotDivide` n | m <- [2..(n-1)], m^2 < n]
    where doesNotDivide a b = (b `mod` a) /= 0

-- |Brute-force solution for calculating the Nth prime.
bruteForceSolution :: Int -> Int
bruteForceSolution n = [m | m <- [2..], isPrimeTD m] !! (n - 1)
