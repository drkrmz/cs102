def encrypt_caesar(plaintext: str) -> str:
    """
    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ''
    for symbol in plaintext:
        if "A" <= symbol <= "W" or "a" <= symbol <= "w":
            ciphertext = ciphertext + chr(ord(symbol)+3)
        elif "X" <= symbol <= "Z" or "x" <= symbol <= "z":
            ciphertext = ciphertext + chr(ord(symbol)-23)
        else:
            ciphertext = ciphertext + chr(ord(symbol))
    return ciphertext


def decrypt_caesar(ciphertext: str) -> str:
    """
    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ''
    for symbol in ciphertext:
        if "D" <= symbol <= "Z" or "d" <= symbol <= "z":
            plaintext = plaintext + chr(ord(symbol)-3)
        elif "A" <= symbol <= "C" or "a" <= symbol <= "c":
            plaintext = plaintext + chr(ord(symbol)+23)
        else:
            plaintext = plaintext + chr(ord(symbol))
    return plaintext
