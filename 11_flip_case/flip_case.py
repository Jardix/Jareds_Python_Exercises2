def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    # My attempt, which did not work. The only thing I could think of to 'fix' this is to make a new string and pass the lower/upper letters into it. 
    # for letter in phrase:
    #     if letter.islower():
    #         letter.upper()
    #     else:
    #         letter.lower()
    # return phrase

    # Solution:
    
    to_swap = to_swap.lower()
    out = ""

    for ltr in phrase:
        if ltr.lower() == to_swap:
            ltr = ltr.swapcase()
        out += ltr

    return out
