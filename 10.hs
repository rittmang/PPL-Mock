add :: Integer -> Integer -> Integer
add x y = x + y

sub :: Integer -> Integer -> Integer
sub x y = x - y

mul :: Integer -> Integer -> Integer
mul x y = x * y

divide :: Integer -> Integer -> Float
divide x y = (fromIntegral x) / (fromIntegral y)

determiner ch a b
    | ch == 1 = print (add a b)
    | ch == 2 = print (sub a b)
    | ch == 3 = print (mul a b)
    | ch == 4 = print (div a b)
    
    
main = do
    putStrLn "Enter numbers:"
    a <- readLn 
    b <- readLn
    putStrLn "Enter choice: 1. Addition 2.Subtraction 3. Multiplication 4. Division"
    choice <- readLn
    determiner choice a b
