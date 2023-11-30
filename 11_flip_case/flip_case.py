def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    flip_phrase = ''
    for letter in phrase:
        if letter.lower() == to_swap.lower():
            if letter.islower() == True:
                flip_phrase = flip_phrase + letter.upper()
            else:
                flip_phrase = flip_phrase + letter.lower()
        else:
            flip_phrase = flip_phrase + letter
    return flip_phrase
