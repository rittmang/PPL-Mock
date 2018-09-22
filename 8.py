#Menu-driven program to implement basic calculator - basic operations in Python
def menu():
    print ("Welcome to Basic Operations in Python")
    print ("1) Addition")
    print ("2) Subtraction")
    print ("3) Multiplication")
    print ("4) Division")
    print ("5) Quit")
    print (" ")
    return input("Choose your option: ")

def add(a,b):
    print a, "+", b, "=", a + b

def sub(a,b):
    print a, "-", b, "=", a - b

def mul(a,b):
    print a, "*", b, "=", a * b

def div(a,b):
    print a, "/", b, "=", a / b

loop = 1
choice = 0
while loop == 1:
    choice=menu()
    if choice == 1:
        add(input("Add this: "),input("to this: "))

    elif choice == 2:
        sub(input("Subtract this: "),input("from this: "))
    elif choice == 3:
        mul(input("Multiply this: "),input("by this: "))
    elif choice == 4:
        div(input("Divide this: "),input("by this: "))
    elif choice == 5:
        loop=0

print ("Done.")
