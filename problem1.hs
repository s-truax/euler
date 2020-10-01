import System.Environment(getArgs)

isMultiple :: Int -> Int -> Bool
isMultiple n 0 = error "No number is a multiple of 0."
isMultiple n m = n `mod` m == 0

solution :: Int -> Int
solution 0 = 0
solution n = sum [k | k <- [1..n],  isMultiple k 3 || isMultiple k 5]

main = do
    args <- getArgs
    print .  solution $ read . head $  args
