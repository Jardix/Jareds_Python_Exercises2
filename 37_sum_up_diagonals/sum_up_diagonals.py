def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """
    total = 0

    for i in range(len(matrix)):
        total += matrix[i][i]
        total += matrix[i][-1 - i]

    return total

    # My attempt to work out this logic. 
    # for m2:
    # total = 0

    # for i in range(len(matrix)):
    #     total += matrix[0][0] = 1
    #     total += matrix[0][-1 - 0] = 3

    # total = 4

    # for i in range(len(matrix)):
    #     total += matrix[1][1] = 5
    #     total += matrix[1][-1 - 1] = 5

    # total = 14

    # for i in range(len(matrix)):
    #     total += matrix[2][2] = 9
    #     total += matrix[2][-1 - 2] = 7

    # toal = 30

    # So, yeah, I could have worked out logic for a 3X3 on my own, eventually, but this logic is way better than my 100 lines of code that would have accomplished nearly the same thing. 
