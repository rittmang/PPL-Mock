factorial n = 
    if n == 0
      then 1
    else n*factorial(n-1)

--main::IO()
main = do
    putStrLn "Enter a number:"
    x <- readLn
    putStrLn(show(x) ++ "! (Recursive)=" ++ show(factorial x))
    -- putStrLn can only output a string. show(x) converts x to a string, ++ to append, show(factorial x) converts output of factorial into a string
    
-- in ghci, :l file.hs to load.    :m to unload module from ghci, gets back to Prelude>
