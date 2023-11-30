def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """
    low_phrase = phrase.lower()
    low_phrase = low_phrase.replace(" ","")
    rev_phrase = ''
    for i in range(len(low_phrase)-1,-1,-1):
        rev_phrase = rev_phrase + low_phrase[i]
    if low_phrase == rev_phrase:
        return True
    else:
        return False
    