def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    rev_phrase = ''
    for i in range(len(phrase)-1,-1,-1):
        rev_phrase = rev_phrase + phrase[i]
    return rev_phrase
