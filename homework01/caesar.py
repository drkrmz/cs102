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
            code_symbol = ord(symbol) + shift
            if ord('Z') < code_symbol < ord('a') or code_symbol > ord('z'):
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
        code_symbol = ord(symbol) - shift
        if "A" <= symbol <= "Z" or "a" <= symbol <= "z":
            if ord('Z') < code_symbol < ord('a') or code_symbol < ord('A'):
                plaintext = plaintext + chr(ord(symbol) - shift + 26)
            else:
                plaintext = plaintext + chr(ord(symbol) - shift)
        else:
            plaintext = plaintext + chr(ord(symbol))
    return plaintext
