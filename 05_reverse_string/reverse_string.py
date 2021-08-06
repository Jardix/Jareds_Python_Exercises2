def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    new_list = list(phrase)
    reved_list = reversed(new_list)
    new_str = "".join(reved_list)
    return new_str
