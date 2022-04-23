# Purpose:    Area of Property in Acres

#x is length in feet
#y is width in feet
#z is conversion from feet to acres

z = (43560)

x = int(input("input Length in feet: "))
y = int(input("input width in feet: "))

n = ((x * y) / z)

print ("number of acres: " + format(n))