def list_check(lst):
    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False
    """
    #  When I wrote this, I had the logic reversed, so that we were checking if isinstance() was true, or returning false at the end. It didn't work, but this did. Not sure why.

    for counter in lst:
        if not isinstance(counter, list):
            return False
    return True
