import math

def polysum(n, s):
    '''
    This function sum the area and square of the perimeter of the regular polygon,
    rounded to 4 decimal places
    Input: n, number of sides
    Input: s, length of each side
    Output: sum the area and square of the perimeter of the regular polygon
    '''
    # The area of regular polygon
    area = 0.25 * n * s ** 2 / math.tan(math.pi / n)
    # The perimeter of a polygon
    perimeter = n*s

    # Return the required sum, rounded to 4 decimal places
    return round(area + perimeter**2, 4)

# Tests
if __name__ == "__main__":
    print(polysum(70, 70))
    print(polysum(20, 7))
    print(polysum(32, 93))
    print(polysum(7, 91))
    print(polysum(28, 68))
    print(polysum(26, 23))
    print(polysum(49, 60))
    print(polysum(89, 41))
    print(polysum(11, 33))
    print(polysum(16, 70))
