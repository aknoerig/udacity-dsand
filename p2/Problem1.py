import math

def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    def _sqrt(number, counter):
        square = counter * counter
        if square == number:
            return counter
        if square > number:
            return counter - 1
        return _sqrt(number, counter + 1)

    return _sqrt(number, 0)

print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (1 == sqrt(2)) else "Fail")
print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")