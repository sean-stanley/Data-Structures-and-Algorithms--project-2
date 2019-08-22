import unittest


def sqrt_rough_estimation(num):
    """
    Calculate a rough sqrt estimate based on size of num.

    Args:
        num(int): Number to have the square root estimated
    Returns:
        int: sqrt estimate

    Credit: https://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Rough_estimation
    """

    # first convert to scientific notation with an even base

    num_str = str(num)

    digits = len(num_str)

    e = digits - 1

    if e % 2 == 0:
        return 2 * 10**(e // 2)

    return 6 * 10**((e - 1)//2)


def sqrt(num):
    """
    Calculate the floored square root of a number.

    Args:
       num(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """

    if num < 0:
        return Exception("Can't find the square root of a negative number.")
    if num == 0:
        return 0
    if num == 1:
        return 1

    seed = sqrt_rough_estimation(num)

    sqrt_value = sqrt_babylon(seed, num, 1)
    return int(sqrt_value)

def sqrt_babylon(previous, num, count):
    """
    Babylonian method of approximating square roots.

    Every iteration produces a more accurate result based on the value
        of previous.

    Args:
        previous(int): the guess used in the previous iteration.
        num(int): the original number we are finding the square root of.
        count(int): the number of attempts so far. We can provide a max to stop
            after a certain number of attempts (for irrational numbers).
    Returns:
        (float): a decimal number

    credit:
    https://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Babylonian_method
    """
    max_attempts = len(str(num)) + 1
    iteration = 0.5 * (previous + num / previous)

    if iteration == previous or count >= max_attempts:
        return iteration

    return sqrt_babylon(iteration, num, count + 1)


print("Pass" if  (5 == sqrt(30)) else "Fail")  # 5
print("Pass" if  (354 == sqrt(125348)) else "Fail")  # 354
print("Pass" if (sqrt(45999234235827) == 6782273) else "Fail")  # 6782273

# edgy cases
print("Pass" if (sqrt(1) == 1) else "Fail")  # 1
print(sqrt(-1))  # Can't find the square root of a negative number.
