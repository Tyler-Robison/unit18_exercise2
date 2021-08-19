def find_greater_numbers(nums):
    """Return # of times a number is followed by a greater number.

    For example, for [1, 2, 3], the answer is 3:
    - the 1 is followed by the 2 *and* the 3
    - the 2 is followed by the 3

    Examples:

        >>> find_greater_numbers([1, 2, 3])
        3

        >>> find_greater_numbers([6, 1, 2, 7])
        4

        >>> find_greater_numbers([5, 4, 3, 2, 1])
        0

        >>> find_greater_numbers([])
        0
    """
    num_count = 0
    for count, num in enumerate(nums):
        num1 = num
        nums = nums[count:]
        for num2 in nums:
            if num2 > num1:
                num_count += 1

    return num_count

    # in inner loop, slice all nums that have already been gone over