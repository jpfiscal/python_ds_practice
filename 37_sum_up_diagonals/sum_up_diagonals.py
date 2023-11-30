def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """
    topleft_btmright = 0
    topright_btmleft = 0
    for i in range(0,len(matrix)):
        topleft_btmright = topleft_btmright + matrix[i][i]
        topright_btmleft = topright_btmleft + matrix[i][len(matrix)-1-i]
    return topleft_btmright + topright_btmleft
