plaintext = input()
def encrypt_ceasar(plaintext):
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
    print(ciphertext) # return ciphertext
encrypt_ceasar(plaintext)

