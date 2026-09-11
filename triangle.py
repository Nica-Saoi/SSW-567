def classify_triangle(a, b, c):
    """Classify a triangle based on its three side lengths."""

    # see if the sides can make a triangle
    if a <= 0 or b <= 0 or c <= 0:
        return "Not a Triangle"

    if a + b <= c or a + c <= b or b + c <= a:
        return "Not a Triangle"

    # figure out triangle type
    if a == b and b == c:
        triangle_type = "Equilateral"

    elif a == b or a == c or b == c:
        triangle_type = "Isosceles"

    else:
        triangle_type = "Scalene"

    # Check if it's also a right triangle
    sides = sorted([a, b, c])

    if sides[0]**2 + sides[1]**2 == sides[2]**2:
        return triangle_type + " and Right"

    return triangle_type

