def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    assert(len(ints) > 0)
    min = ints[0]
    max = min
    for i in range(0, len(ints)):
        num = ints[i]
        if num < min:
            min = num
        if num > max:
            max = num   
    return min, max

## Test Cases
import random

#print(get_min_max([]))
# AssertionError
print(get_min_max([0]))
# (0, 0)
print(get_min_max([0,0]))
# (0, 0)
print(get_min_max([0,-1]))
# (-1, 0)

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)
print (get_min_max(l))
# (0, 9)

l = [i for i in range(0, 1000)]  # a list containing 0 - 999
random.shuffle(l)
print (get_min_max(l))
# (0, 999)