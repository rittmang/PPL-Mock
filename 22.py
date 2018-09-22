#Computes result from marks of 3 subjects
def result(m):
    if m > 80:
        print("\nYou passed with distinction!")

    elif m <= 80 & m > 60:
        print("\nYou passed with First Class!")

    elif m <=60 & m > 50:
        print("\nYou passed with Second Class.")

    elif m<=50 & m > 40:
        print("\nYou passed.")

    else:
        print("\nYou failed.")

def average(temp_one,temp_two,temp_three):
    return (temp_one + temp_two + temp_three) / 3.0


print("Enter marks for 3 subjects:")
name=(raw_input("Name:"))
a=int(input("1st subject:"))
b=int(input("2nd subject:"))
c=int(input("3rd subject:"))
avg=average(a,b,c)
print "Name=",name
print("\nYour average mark is:" '{:.1f}'.format(avg))
result(avg)
