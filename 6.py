def factoi (n):
    if n == 0:
        return 1
    elif n > 0:
        f=1;
        for i in range (1,n+1): # n+1 as range takes from 1(inclusive) to n (exclusive)
            f*=i
        return f;
    else:
        return "WRONG NUMBER INPUT"

def factor (n):
    if n == 0:
        return 1
    elif n > 0:
        return n*factor(n-1)
    else:
        return "WRONG NUMBER INPUT"

n=int(input("Enter number:"))
print("1. Iterative  2. Recursive")
choice=int(input("Enter choice:"))
if choice == 1:
    print("\n",n,"! (Iterative)=",factoi(n))

elif choice == 2:
    print("\n",n,"! (Recursive)=",factor(n))
else:
    print("Wrong choice option.")


#Run in Python3 for correct implementation of print("",x,y,"=",func(x)) Like that
#in Python2, print "",x,y,func(x)  Like that. No brackets.
