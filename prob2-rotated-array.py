
def rotated_array_search(input_list, number, start_index, end_index):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    if start_index > end_index:
        return -1

    mid_index = (start_index + end_index) // 2

    if input_list[mid_index] == number:
        return mid_index

    # check if first half is sorted
    if input_list[start_index] < input_list[mid_index]:
        if input_list[start_index] <= number < input_list[mid_index]:
            return rotated_array_search(input_list, number, start_index, mid_index-1)
        return rotated_array_search(input_list, number, mid_index+1, end_index)

    # if first half is not sorted than second half must be
    if input_list[mid_index] < number <= input_list[end_index]:
        return rotated_array_search(
            input_list, number, mid_index + 1, end_index
        )
    return rotated_array_search(input_list, number, start_index, mid_index - 1)


def linear_search(input_list, number):
    """O(n) approarch for testing"""
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    output = rotated_array_search(
        input_list,
        number,
        0,
        len(input_list) - 1
    )
    solution = linear_search(input_list, number)
    if output == solution:
        print(f"Pass, {output}")
    else:
        print(f"Fail, {output}")


test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])  # 0
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])  # 5
test_function([[6, 7, 8, 1, 2, 3, 4], 8])  # 2
test_function([[6, 7, 8, 1, 2, 3, 4], 1])  # 3
test_function([[6, 7, 8, 1, 2, 3, 4], 10])  # -1
test_function([[10, 11, 12, 13, 14, 15, 16, 1, 2, 3, 4, 5, 6, 7, 8, 9], 2])  # 8
