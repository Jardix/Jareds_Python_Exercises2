def remove_every_other(lst):
    """Return a new list of other item.

        >>> lst = [1, 2, 3, 4, 5]

        >>> remove_every_other(lst)
        [1, 3, 5]

    This should return a list, not mutate the original:

        >>> lst
        [1, 2, 3, 4, 5]
    """
    #  Mine is longer, as usual, but I prefer it as it seems to have more... reliability? There's more possibilities and less chance of edge cases? I think.
    new_list = []

    new_list.append(lst[::2])
    return new_list
