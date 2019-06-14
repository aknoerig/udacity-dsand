def rotated_array_search(input_list, target):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), target(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    def binary_search(input_list, target, left, right):
        if left > right:
            return -1
        middle = (left + right) // 2
        middle_value = input_list[middle]

        if middle_value == target:
            return middle
        if target < middle_value:
            return binary_search(input_list, target, left, middle - 1)
        return binary_search(input_list, target, middle + 1, right)

    def pivot_search(input_list, left, right):
        if left > right:
            return -1
        if left == right:
            return left
        middle = (left + right) // 2
        middle_value = input_list[middle]
        
        if middle < right and middle_value > input_list[middle + 1]:
            return middle
        if middle > left and middle_value < input_list[middle - 1]:
            return pivot_search(input_list, left, middle - 1)
        return pivot_search(input_list, middle + 1, right)

    if len(input_list) < 1:
        return -1

    pivot = pivot_search(input_list, 0, len(input_list) - 1)
    if pivot == -1:
        return binary_search(input_list, target, 0, len(input_list - 1))

    pivot_value = input_list[pivot]
    if target == pivot_value:
        return pivot
    if target < pivot_value and target >= input_list[0]:
        return binary_search(input_list, target, 0, pivot)
    return binary_search(input_list, target, pivot + 1, len(input_list) - 1)

def linear_search(input_list, target):
    for index, element in enumerate(input_list):
        if element == target:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    target = test_case[1]
    output = rotated_array_search(input_list, target)
    print(output)
    if linear_search(input_list, target) == output:
        print("Pass")
    else:
        print("Fail")

test_function([[], 0])
# -1
test_function([[1], 1])
# 0
test_function([[1, 2, 3], 2])
# 1

test_function([[3, 1, 2], 3])
# 0
test_function([[3, 1, 2], 1])
# 1
test_function([[3, 1, 2], 2])
# 2

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
# 0
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
# 5
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 4])
# 8

test_function([[6, 7, 8, 9, 10, 11, 12, 3, 4], 7])
# 1
test_function([[6, 7, 8, 9, 10, 11, 12, 3, 4], 3])
# 7

test_function([[6, 7, 8, 9, 1, 2, 3, 4], 8])
# 2
test_function([[6, 7, 8, 9, 1, 2, 3, 4], 3])
# 6
test_function([[6, 7, 8, 9, 1, 2, 3, 4], 10])
# -1