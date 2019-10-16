def encrypt_caesar(plaintext: str, shift: int) -> str:
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
        if "A" <= symbol <= "Z" or "a" <= symbol <= "z":
            if ord('Z') < ord(symbol) + shift < ord('a') or ord(symbol) + shift > ord('z'):
                ciphertext = ciphertext + chr(ord(symbol) + shift - 26)
            else:
                ciphertext = ciphertext + chr(ord(symbol) + shift)
        else:
            ciphertext = ciphertext + chr(ord(symbol))
    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int) -> str:
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
        if "A" <= symbol <= "Z" or "a" <= symbol <= "z":
            if ord('Z') < ord(symbol) - shift < ord('a') or ord(symbol) - shift < ord('A'):
                plaintext = plaintext + chr(ord(symbol)- shift + 26)
            else:
                plaintext = plaintext + chr(ord(symbol) - shift)
        else:
            plaintext = plaintext + chr(ord(symbol))
    return plaintext
