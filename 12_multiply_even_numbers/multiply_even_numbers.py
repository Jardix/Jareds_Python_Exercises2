def multiply_even_numbers(nums):
    """Multiply the even numbers.

        >>> multiply_even_numbers([2, 3, 4, 5, 6])
        48

        >>> multiply_even_numbers([3, 4, 5])
        4

    If there are no even numbers, return 1.

        >>> multiply_even_numbers([1, 3, 5])
        1
    """
    # Got lost in the logic of this one.
    # list_of_nums = [1]

    # for num in nums:
    #     if num % 2 == 0:
    #         list_of_nums.push(num)
    #         # Multiply the first element by any elements that are pushed in? Not sure how to do that.

    #  Solution: I was so close...
    product = 1

    for num in nums:
        if num % 2 == 0:
            product = product * num

    return product
