{-|
  An implementation of the Sieve of Eratosthenes that uses
  list comprehension (i.e. filtering) to do the bulk of the work.

  Counts the number of primes less than or equal to N.
-}
filterSieve :: Int -> Int
filterSieve n = let
    doesNotDivide     x y  = y `mod` x /= 0
    filterSieveHelper p xs =
        let sieved = [m | m <- xs, p `doesNotDivide` m]
            nextP  = head sieved
        in  if  p^2 > n || null sieved
                then xs
                else filterSieveHelper nextP sieved
    in length $  filterSieveHelper 2 [1..n]

{-
Not sure why I can't use function composition here:

problem7.hs:16:17: error:
    • Couldn't match expected type ‘a1 -> t0 a0’
                  with actual type ‘[Int]’
    • Possible cause: ‘filterSieveHelper’ is applied to too many arguments
      In the second argument of ‘(.)’, namely
        ‘filterSieveHelper 2 [1 .. n]’
      In the expression: length . filterSieveHelper 2 [1 .. n]
      In the expression:
        let
          doesNotDivide x y = y `mod` x /= 0
          filterSieveHelper p xs = let ... in ...
        in length . filterSieveHelper 2 [1 .. n]
   |
16 |     in length . filterSieveHelper 2 [1..n]
   |                 ^^^^^^^^^^^^^^^^^^^^^^^^^^
-}

