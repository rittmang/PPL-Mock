def area_table(l,b):
    return l*b

#def perim_table(l,b):
 #   return 2*(l+b)

print("Enter dimensions of the TT table:")
x=int(input("Enter length:"))
y=int(input("Enter breadth:"))

print "\nArea of the TT table=", area_table(x,y), " unit^2" #this works in Python2 only. Syntax error in Python3, thus use as print("",area_table(x,y),"unit^2")

#print "Perimeter of the table=", perim_table(x,y), "units"
