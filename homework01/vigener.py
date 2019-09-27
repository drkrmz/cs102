def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ''
    i = 0
    while i < len(plaintext):
        symbol = plaintext[i]
        shift = keyword [i % len(keyword)]
        if ord(shift) in range(65, 91):
            if ord(symbol)+ord(shift)-65 < 91:
                ciphertext = ciphertext + chr(ord(shift)+ord(symbol)-65)
            else:
                ciphertext = ciphertext + chr(ord(shift)+ord(symbol)-65-26)
        else:
            if ord(symbol)+ord(shift)-97 < 123:
                ciphertext = ciphertext + chr(ord(shift)+ord(symbol)-97)
            else:
                ciphertext = ciphertext + chr(ord(shift)+ord(symbol)-97-26)
        i = i + 1
    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ''
    i = 0
    while i < len(ciphertext):
        symbol = ciphertext[i]
        shift = keyword [i % len(keyword)]
        if ord(shift) in range(65, 91):
            if ord(symbol)-ord(shift)+65 > 64:
                plaintext = plaintext + chr(ord(symbol)-ord(shift)+65)
            else:
                plaintext = plaintext + chr(ord(symbol)-ord(shift)+65+26)
        else:
            if ord(symbol)-ord(shift)+97 > 96:
                plaintext = plaintext + chr(ord(symbol)-ord(shift)+97)
            else:
                plaintext = plaintext + chr(ord(symbol)-ord(shift)+97+26)
        i = i + 1
    return plaintext
