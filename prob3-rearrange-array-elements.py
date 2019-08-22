def merge_reverse(left, right):
    """
    Merge two lists in order of highest-to-lowest.

    left @int<[]> lists of integers to be merged
    right @int<[]> lists of integers to be sorted

    return @int<[]> list of integers
    """
    if not left or not right:
        return left or right

    result = []
    left_index, right_index = 0, 0

    while len(result) < len(left) + len(right):
        # test with ">" to sort largest to smallest
        if left[left_index] > right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1
        if left_index == len(left) or right_index == len(right):
            result.extend(left[left_index:] or right[right_index:])
            break

    return result


def mergesort_reverse(input_list):
    """
    Merge sort using the last element as a pivot.

    input_list @int<[]> list of integers.

    returns a new List with values ordered from highest, to lowest
    """
    if len(input_list) <= 1:
        return input_list

    middle = len(input_list)//2
    left = mergesort_reverse(input_list[:middle])
    right = mergesort_reverse(input_list[middle:])

    return merge_reverse(left, right)


def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    if not input_list:
        return []

    num1, num2 = '', ''
    input_list = mergesort_reverse(input_list)

    # use sorted list to assemble the 2 numbers
    for idx, value in enumerate(input_list):
        if value > 9 or value < 0:
            return 'all inputs should be between 0-9'
        if idx % 2 == 0:
            num1 += str(value)
        else:
            num2 += str(value)

    return [int(num1), int(num2)]


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if isinstance(solution, str):
        print(output)
    elif sum(output) == sum(solution):
        print(f"Pass, {output}")
    else:
        print(f"Fail, {output}")

test_case1 = [[4, 6, 2, 5, 9, 8], [964, 852]]
test_case2 = [[10, 2, -3, 40, 5], 'all inputs should be between 0-9']
test_case3 = [None, []]
test_case4 = [[3,0,9,9,3,4,6,7,3,2,5,1], [975331, 964320]]

test_function(test_case1)  # [964, 852]
test_function(test_case2)  # 'all inputs should be between 0-9'
test_function(test_case3)  # [] edgy None value
test_function(test_case4)  # [975331, 96432] edgy duplicate values
