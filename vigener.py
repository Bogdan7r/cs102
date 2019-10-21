plaintext = input()
key = input()
def  encrypt_vigenere(plaintext, key):
     """
     >>> encrypt_vigenere("PYTHON", "A")
     'PYTHON'
     >>> encrypt_vigenere("python", "a")
     'python'
     >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
     'LXFOPVEFRNHR'
     """
     alfavit = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
     long_plaintext = len(plaintext)
     long_key = len(key)
     k = ((long_plaintext) // (long_key)) +1
     key = k*key
     k = 0
     t = 0 
     job_key = ""
     ciphertext = ""
     while k != long_plaintext:
         job_key += key[k]
         k +=1             
     job_key = job_key.upper() # Сейчас у нас есть подходящие фраза и ключ для реализации шифра
     
     for i in job_key:
         for x in alfavit:
            if i == x:
                k = alfavit.index(x)
                if ((ord(plaintext[t])+k) > 90) and ((ord(plaintext[t]) < 91 )):
                    ciphertext += chr(ord(plaintext[t])+k-26)
                if ((ord(plaintext[t])+k) > 122):
                    ciphertext += chr(ord(plaintext[t])+k-26)
                if ((ord(plaintext[t])+k) < 90):
                    ciphertext += chr(ord(plaintext[t])+k)
                if ((ord(plaintext[t])+k) < 122) and (ord(plaintext[t]) > 90):
                    ciphertext += chr(ord(plaintext[t])+k)
                t +=1
     print(ciphertext)
       
encrypt_vigenere(plaintext, key)

ciphertext = input()
key = input()
def  decrypt_vigenere(ciphertext, key):
     """
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
     alfavit = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
     long_ciphertext = len(ciphertext)
     long_key = len(key)
     k = ((long_ciphertext) // (long_key)) +1
     key = k*key
     k = 0
     t = 0 
     job_key = ""
     plaintext = ""
     while k != long_ciphertext:
         job_key += key[k]
         k +=1             
     job_key = job_key.upper() # Сейчас у нас есть подходящие фраза и ключ для реализации шифра
     
     for i in job_key:
         for x in alfavit:
            if i == x:
                k = alfavit.index(x)
                if ((ord(ciphertext[t])-k) < 65):
                    plaintext += chr(ord(ciphertext[t])-k+26)
                if ((ord(ciphertext[t])-k) > 64) and (ord(ciphertext[t]) < 91):
                    plaintext += chr(ord(ciphertext[t])-k)
                if ((ord(ciphertext[t])-k) < 96) and ((ord(ciphertext[t])) > 96):
                    plaintext += chr(ord(ciphertext[t])-k+26)
                if ((ord(ciphertext[t])) < 123) and ((ord(ciphertext[t])-k) > 96):
                    plaintext += chr(ord(ciphertext[t])-k)
                t +=1
     print(plaintext)
decrypt_vigenere(ciphertext, key) 



     
