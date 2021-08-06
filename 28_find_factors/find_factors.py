def find_factors(num):
    """Find factors of num, in increasing order.

    >>> find_factors(10)
    [1, 2, 5, 10]

    >>> find_factors(11)
    [1, 11]

    >>> find_factors(111)
    [1, 3, 37, 111]

    >>> find_factors(321421)
    [1, 293, 1097, 321421]
    """
    # This is the modified version of what I originally wrote; I never did use while loops that much before. But why did they not initialize 'n' in the solution?

    # fac_list = []
    
    # while(n <= num):
    #     if num % n == 0:
    #         fac_list.append(n)
    #     n += 1

    # return fac_list

    # Solution:

    # n_list = [n for n in range (1, num // 2 + 1) if num % n == 0]

    # n_list.append(num)

    # return n_list

    # or could write by hand with a while loop
    #
    factors = []
    n = 1
    while(n <= num):
        if num % n == 0:
            factors.append(n)
        n += 1
    
    return factors
