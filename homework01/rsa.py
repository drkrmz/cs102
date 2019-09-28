from typing import Tuple

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
    return is_prime

def gcd(a: int, b: int) -> int:
    """
    >>> gcd(12, 15)
    3
    >>> gcd(3, 7)
    1
    """
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        elif b > a:
            b = b % a
    if a == 0:
        gcd = b
    else:
        gcd = a
    return gcd

def multiplicative_inverse(e: int, phi: int) -> int:
    """
    >>> multiplicative_inverse(7, 40)
    23
    """
    div = []
    phi1 = phi
    while e!=0 and phi!=0:
        if e > phi:
            div.append(e // phi)
            e = e % phi
        else:
            div.append(phi // e)
            phi = phi % e
    dl = len(div) - 1
    x = 1
    y = 0
    for i in range(dl):
        y1 = y
        y = x
        x = y1 - x * div[dl-i-1]
    multiplicative_inverse = x % phi1
    return multiplicative_inverse

def generate_keypair(p: int, q: int) -> Tuple[Tuple[int, int], Tuple[int, int]]:
    if not (is_prime(p) and is_prime(q)):
        raise ValueError('Both numbers must be prime.')
    elif p == q:
        raise ValueError('p and q cannot be equal')

    # n = pq
    n = p * q

    # phi = (p-1)(q-1)
    phi = (p-1) * (q-1)

    # Choose an integer e such that e and phi(n) are coprime
    e = random.randrange(1, phi)

    # Use Euclid's Algorithm to verify that e and phi(n) are comprime
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)

    # Use Extended Euclid's Algorithm to generate the private key
    d = multiplicative_inverse(e, phi)
    # Return public and private keypair
    # Public key is (e, n) and private key is (d, n)
    return ((e, n), (d, n))