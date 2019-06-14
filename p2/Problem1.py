import math

def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    def approx_sqrt(number, root):
        delta = number - (root * root)
        if 0 <= delta < 0.1:
            return root
        if delta < 0:
            return approx_sqrt(number, root / 2)
        if delta > 0:
            return approx_sqrt(number, root * 3 / 2)
    
    def newton_sqrt(number):
        x = number
        y = (x + 1) // 2
        while y < x:
            x = y
            y = (x + number // x) // 2
        return x

    if number == 0:
        return 0
    if number == 1:
        return 1
    #return approx_sqrt(number, number / 2)
    return newton_sqrt(number)

print(sqrt(0))
# 0
print(sqrt(1))
# 1 *
print(sqrt(2))
# 1
print()

print(sqrt(3))
# 1
print(sqrt(4))
# 2 *
print(sqrt(5))
# 2
print()

print(sqrt(8))
# 2
print(sqrt(9))
# 3 *
print(sqrt(10))
# 3
print()

print(sqrt(15))
# 3
print(sqrt(16))
# 4 *
print(sqrt(17))
# 4
print()

print(sqrt(24))
# 4
print(sqrt(25))
# 5 *
print(sqrt(26))
# 5