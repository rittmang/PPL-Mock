#def area_ground(l,b):
 #   return l*b

def perim_ground(l,b):
    return 2*(l+b)

print("Enter dimensions of the football ground:")
x=int(input("Enter length:"))
y=int(input("Enter breadth:"))

#print "\nArea of the football ground=", area_ground(x,y), " unit^2"

print "Perimeter of the football ground=", perim_ground(x,y), "units"
 #this works in Python2 only. Syntax error in Python3, thus use as print("",perim_pitch(x,y),"unit^2")
