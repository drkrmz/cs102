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
        if ord(symbol) in range(65, 88) or ord(symbol) in range(97, 120):
            ciphertext = ciphertext + chr(ord(symbol)+3)
        elif ord(symbol) in range(88, 91) or ord(symbol) in range(120, 123):
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
    # PUT YOUR CODE HERE
    return plaintext
