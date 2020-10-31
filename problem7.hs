import System.Environment

-- Possibly inefficient, tried to implement it on my own before importing.
deleteFirstsBy :: (a -> a -> Bool) -> [a] -> [a] -> [a]
deleteFirstsBy _ xs [] = xs
deleteFirstsBy _ [] _  = []
deleteFirstsBy eq (x:xs) (y:ys) = 
   if x `eq` y
     then deleteFirstsBy eq xs ys
       else (deleteFirstsBy eq [x] ys) ++ (deleteFirstsBy eq xs (y:ys))

listDiff :: Eq a => [a] -> [a] -> [a]
listDiff = deleteFirstsBy (==)


gcd' :: Int -> Int -> Int
gcd' a 0 = a
gcd' 0 b = b
gcd' a b = gcd b (a `mod` b)


finiteSieve' :: [Int] -> [Int] -> Int -> [Int]
finiteSieve' primes []     n  = primes
finiteSieve' primes (x:xs) n = let
    p = x
    sifted = listDiff xs [p^2, p^2 + p..n] in
    if p^2 > n
        then (reverse primes) ++ xs
          else
            finiteSieve' (p : primes) sifted n


-- this... is wrong, I think.
finiteSieve :: Int -> [Int]
finiteSieve n = finiteSieve' [] [2, 3..n] n

{-|
  An implementation of the Sieve of Eratosthenes that uses
  list comprehension (i.e. filtering) to do the bulk of the work.

  Finds all primes less than or equal to N.

  UPDATE (10/27/2020): This is actually not a proper sieve of Eratosthenes,
  since I'm explicity checking for primality. The true sieve does not employ
  any kind of primality test.
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
--  This is surprisingly fast for n <= 10^100000. Why? (It's also fast in Python)
isPrimeTD :: Int -> Bool
isPrimeTD n
    | n <= 1    = False
    | otherwise = and [m `doesNotDivide` n | m <- [2..(n-1)], m^2 < n]
    where doesNotDivide a b = (b `mod` a) /= 0

-- |Brute-force solution for calculating the Nth prime.
bruteForceSolution :: Int -> Int
bruteForceSolution n = [m | m <- [2..], isPrimeTD m] !! (n - 1)

main = do
    args <- System.Environment.getArgs
    print $ finiteSieve $ read $ head args
