def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    new_str = ''
    for char in phrase:
        if char.lower() == to_swap or char.upper() == to_swap:
            if char == char.upper():
                char = char.lower()
                new_str+=char
            elif char == char.lower():
                char = char.upper()    
                new_str+=char              
        else:
            new_str+=char
    return new_str