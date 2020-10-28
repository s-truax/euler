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

-- BROKEN: This is quite hard to do with a list, since you need to figure out how to
-- keep updating p.
finiteSieveHelper :: Integer -> [Integer] -> Integer -> [Integer]
finiteSieveHelper p acc n
    | p^2 > n   = acc
    | otherwise = finiteSieveHelper nextP newAcc n
    where newAcc = tail $ listDiff acc [p^2,p^2 + p..n]
          nextP  = head newAcc


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


