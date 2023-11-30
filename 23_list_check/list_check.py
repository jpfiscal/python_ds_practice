def list_check(lst):
    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False
    """
    list_list = [l for l in lst if isinstance(l, list)]
    return len(list_list) == len(lst)