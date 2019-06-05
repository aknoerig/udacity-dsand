import math

def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    def _sqrt(number, root):
        delta = (number / root) - root
        if abs(delta) < 1:
            return math.floor(root)
        if delta < 0:
            return _sqrt(number, root / 2)
        if delta > 0:
            return _sqrt(number, root * 3 / 2)

    if number == 0:
        return 0
    if number == 1:
        return 1
    return _sqrt(number, number / 2)

print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (1 == sqrt(2)) else "Fail")
print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")