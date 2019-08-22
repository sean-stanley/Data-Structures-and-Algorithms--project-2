import math
import random

def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    curr_min = math.inf
    curr_max = -math.inf

    for num in ints:
        if int(num) > curr_max:
            curr_max = num
        if int(num) < curr_min:
            curr_min = num

    return (int(curr_min), int(curr_max))


# Example Test Case of Ten Integers

def tests():
    """Print "Pass" for 1 straightforward test and 2 edge cases."""
    # test 1
    list_of_ints = [i for i in range(0, 10)]  # a list containing 0 - 9
    random.shuffle(list_of_ints)
    print("Pass" if ((0, 9) == get_min_max(list_of_ints)) else "Fail")

    # test 2 (edgy) negative numbers
    list_of_ints = [i for i in range(-10, 0)]
    random.shuffle(list_of_ints)
    print("Pass" if ((-10, -1) == get_min_max(list_of_ints)) else "Fail")

    # test 3 (edgy) floats
    list_of_inputs = [i/2 for i in range(0, 20, 1)]
    random.shuffle(list_of_inputs)
    print("Pass" if ((0, 9) == get_min_max(list_of_inputs)) else "Fail")

    # test 4 (edgy) tiny list
    print("Pass" if ((3, 3) == get_min_max([3.14])) else "Fail")

    # test 4 large ints
    list_of_ints = [i for i in range(-1000, 1000, 10)]
    random.shuffle(list_of_ints)
    print("Pass" if ((-1000, 990) == get_min_max(list_of_ints)) else "Fail")


tests()
