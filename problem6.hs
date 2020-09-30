import System.Environment(getArgs)

sumSquares n  = sum $ map (^2) [1..n]

squareSum  n  = (^2) $ sum [1..n]

solution   n  = squareSum n -  sumSquares n

main = do
    let sol = solution 100
    putStrLn "Solution for n == 100:"
    print sol
