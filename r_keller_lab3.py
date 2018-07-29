x1 = int(input("Enter the x axis of the center of the circle: "))
y1 = int(input("Enter the y axis of the center of the circle: "))
x2 = int(input("Enter the x axis of a point on the circle: "))
y2 = int(input("Enter the y axis of a point on the circle: "))

def distance(w,x,y,z):
    d = (((x2-x1)**2+(y2-y1)**2)**.5)
    return d
d = distance(x1,x2,y1,y2)

def radius(x):
    r = d/2
    return r
r = radius(d)

def circumference(x):
    c = 2*3.1416*r
    return c
c = circumference(r)

def area(x):
    a = 3.1416*r**2
    return a
    print(a)
a = area(r)

print("Radius")
print(r)
print("Diamter")
print(d)
print("Circumference")
print(c)
print("Area")
print(a)





