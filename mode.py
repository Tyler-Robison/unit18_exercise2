def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    counter_dict = {}
    for num in nums:
        counter_dict[num] = counter_dict.get(num, 0) + 1

    max_value = max(counter_dict.values())  

    for (num, freq) in counter_dict.items():
        if freq == max_value:
            return num