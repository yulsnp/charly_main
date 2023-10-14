import math
def area_triangle(b,h):
    areat=b*h/2
    return areat

def area_square(side):
    areac=side*side
    return areac

def area_circle(radius):
    p=math.pi
    areacir=p*radius*radius
    return areacir
    

print(f"The area of the triangle is: {area_triangle(4,5)}")
print(f"The area of the square is: {area_square(4)}")
print(f"The area of the circle is: {area_circle(7)}")
