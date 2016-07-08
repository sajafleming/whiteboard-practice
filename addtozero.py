"""Given list of ints, return True if any two nums in list sum to 0.

    >>> add_to_zero([])
    False

    >>> add_to_zero([1])
    False

    >>> add_to_zero([1, 2, 3])
    False

    >>> add_to_zero([1, 2, 3, -2])
    True

Given the wording of our problem, a zero in the list will always
make this true, since "any two numbers" could include that same
zero for both numbers, and they sum to zero:

    >>> add_to_zero([0, 1, 2])
    True
"""


def add_to_zero(nums):
    """Given list of ints, return True if any two nums in list sum to 0."""

    # since I want to know if the negative of the number is in the list
    # make it a set for O(1) time rather than the O(n) lookup time of list
    set_nums = set(nums)

    for num in nums:
        # don't actually need this since python considers -0 == 0
        if num == 0:
            return True
        elif -num in nums:
            return True
    return False


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. NOTHING ESCAPES YOU!\n"
