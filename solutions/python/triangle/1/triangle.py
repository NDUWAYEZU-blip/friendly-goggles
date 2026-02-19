def equilateral(sides):
    """Function that determines if a triangle is equilateral."""
    a,b,c = sides
    if a <= 0 or b <= 0 or c <= 0:
        return False
    if a == b == c:
        return True
    return False
def isosceles(sides):
    """Function that determines if a triangle is isosceles."""
    a,b,c = sides
    if a <= 0 or b <= 0 or c <= 0:
        return False
    if a + b < c or a + c < b or b + c < a:
        return False
    if a == b or a == c or c == b:
        return True 
    return False
def scalene(sides):
    """Function that determines if a triangle is scalene."""
    a,b,c = sides
    if a <= 0 or b <= 0 or c <= 0:
        return False
    if a + b < c or a + c < b or b + c < a:
        return False
    if a == b or a == c or c == b:
        return False
    return True