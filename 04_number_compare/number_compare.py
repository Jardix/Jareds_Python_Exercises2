def number_compare(a, b):
    """Report on whether a>b, b>a, or b==a

        >>> number_compare(1, 1)
        'Numbers are equal'

        >>> number_compare(-1, 1)
        'Second is greater'

        >>> number_compare(1, -2)
        'First is greater'
    """
    if type(a) == str or type(b) == str:
        return "Please enter two numbers."
    if a == b:
        return 'Numbers are equal'
    if b > a:
        return 'Second is greater'
    if a > b:
        return 'First is greater'
