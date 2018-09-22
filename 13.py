import math
def area_pitch(l,b):
    return l*b

def area_groundCircular(r):
    return math.pi*r*r;

#def perim_pitch(l,b):
 #   return 2*(l+b)

print("Enter dimensions of the cricket pitch:")
x=int(input("Enter length:"))
y=int(input("Enter breadth:"))

r=int(input("Enter radius:"))
print "\nArea of the cricket pitch=", area_pitch(x,y), " unit^2" #this works in Python2 only. Syntax error in Python3, thus use as print("",area_ground(x,y),"unit^2")
print "\nArea of the cricket ground=", area_groundCircular(r), " unit^2"

#print "Perimeter of the pitch=", perim_pitch(x,y), "units"
