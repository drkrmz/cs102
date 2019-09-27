def is_prime(n: int) -> bool:
    """
    >>> is_prime(2)
    True
    >>> is_prime(11)
    True
    >>> is_prime(8)
    False
    """
    prost = 0
    if n % 2 == 0 and n != 2:
        is_prime = False
    else:
        factor = 3
        while factor * factor < n and prost == 0:
            if n % factor == 0:
                prost = 1
            factor = factor + 2
        if prost == 1:
            is_prime = False
        else:
            is_prime = True
    pass