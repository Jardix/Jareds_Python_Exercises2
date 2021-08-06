def frequency(lst, search_term):
    """Return frequency of term in lst.

        >>> frequency([1, 4, 3, 4, 4], 4)
        3

        >>> frequency([1, 4, 3], 7)
        0
    """
    # Absolutely love that I'll read the instructions, think, "Oh wait, I know how to do this!" and type 6 lines of code, only to find out that there's a built in feature to python that does exactly this in one line.
    # Good to know, disappointing none the less.

    counter = 0

    for num in lst:
        if num == search_term:
            counter = counter + 1
    return counter
