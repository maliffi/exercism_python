def equilateral(sides):
    return is_triangle(sides) and (sides[0] == sides[1] and sides[1] == sides[2])

def isosceles(sides):
    return is_triangle(sides) and (sides[0] == sides[1] or sides[0] == sides[2] or sides [1] == sides[2])
    

def scalene(sides):
    return is_triangle(sides) and not equilateral(sides) and not isosceles(sides)

def is_triangle(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]
    if a <=0 or b <= 0 or c <=0:
        return False
    return a+b >= c and a+c >= b and b+c >= a