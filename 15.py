#def area_pitch(l,b):
 #   return l*b

def perim_pitch(l,b):
    return 2*(l+b)

print("Enter dimensions of the cricket pitch:")
x=int(input("Enter length:"))
y=int(input("Enter breadth:"))

#print "\nArea of the cricket pitch=", area_pitch(x,y), " unit^2"

print "Perimeter of the cricket pitch=", perim_pitch(x,y), "units"
 #this works in Python2 only. Syntax error in Python3, thus use as print("",perim_pitch(x,y),"unit^2")
