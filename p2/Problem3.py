def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    def quicksort(array, start, stop):
        if stop - start > 0:
            pivot, left, right = array[start], start, stop
            while left <= right:
                while array[left] < pivot:
                    left += 1
                while array[right] > pivot:
                    right -= 1
                if left <= right:
                    array[left], array[right] = array[right], array[left]
                    left += 1
                    right -= 1
            quicksort(array, start, right)
            quicksort(array, left, stop)

    quicksort(input_list, 0, len(input_list) - 1)
    
    sum1 = 0
    sum2 = 0
    i = 0
    factor = 1

    while i < len(input_list):
        sum1 += input_list[i] * factor
        if i + 1 < len(input_list):
            sum2 += input_list[i + 1] * factor
        factor *= 10
        i += 2

    return sum1, sum2

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
test_function([[0, 1], [0, 1]])