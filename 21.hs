oddeven n =
    if n `rem` 2 == 0
      then putStrLn(show(n) ++ " is even.")

    else putStrLn(show(n) ++ " is odd.")


main=do
  putStrLn "Enter a number:"
  x <- readLn
  oddeven x
