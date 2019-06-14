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

    def _sqrt(number, low, high):
        mid = (low + high) // 2
        delta = number - (mid * mid)
        if delta == 0 or low == high:
            return mid
        if high - low == 1:
            if high ** 2 > number:
                return low
            return high
        if delta < 0:
            return _sqrt(number, low, mid)
        if delta > 0:
            return _sqrt(number, mid, high)
    
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
    #return newton_sqrt(number)
    return _sqrt(number, 0, number // 2)

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