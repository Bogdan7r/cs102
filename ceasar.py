plaintext = input()
def encrypt_ceasar(plaintext):
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
    ciphertext = ""
    for i in plaintext:
        if ((ord(i) > 64) and (ord(i) < 91)) or (ord(i) > 96) and (ord(i) < 123):
            if (ord(i) > 64) and (ord(i) < 91):
                if (ord(i)+3) > 90:
                    ciphertext = ciphertext + chr(ord(i)+3-26)
                else:
                    ciphertext = ciphertext + chr(ord(i)+3)

            if (ord(i) > 96) and (ord(i) < 123):
                if (ord(i)+3) > 122:
                    ciphertext = ciphertext + chr(ord(i)+3-26)
                else:
                    ciphertext = ciphertext + chr(ord(i)+3)
        else:
            ciphertext = ciphertext + i
    return ciphertext 

ciphertext = input()
def encrypt_ceasar(ciphertext):
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
    plaintext = ""
    for i in ciphertext:
        if ((ord(i) > 64) and (ord(i) < 91)) or (ord(i) > 96) and (ord(i) < 123):
            if (ord(i) > 64) and (ord(i) < 91):
                if (ord(i)-3) < 65:
                    plaintext = plaintext + chr(ord(i)-3+26)
                else:
                    plaintext = plaintext + chr(ord(i)-3)

            if (ord(i) > 96) and (ord(i) < 123):
                if (ord(i)-3) < 97:
                    plaintext = plaintext + chr(ord(i)-3+26)
                else:
                    plaintext = plaintext + chr(ord(i)-3)
        else:
            plaintext = plaintext + i
    return plaintext 

