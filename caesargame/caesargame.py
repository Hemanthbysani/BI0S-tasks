def cipher_encrypt(plain_text, key):
    encrypted = ""
    for c in plain_text:

        if c.isupper(): 
            c_index = ord(c) - ord('A')
            c_shifted = (c_index + key) % 26 + ord('A')
            c_new = chr(c_shifted)
            encrypted += c_new
        elif c.islower(): 
            c_index = ord(c) - ord('a') 
            c_shifted = (c_index + key) % 26 + ord('a')
            c_new = chr(c_shifted)
            encrypted += c_new
        else:
            encrypted += c
    return encrypted
def cipher_decrypt(ciphertext, key):
    decrypted = ""
    for c in ciphertext:
        if c.isupper(): 
            c_index = ord(c) - ord('A')
            c_og_pos = (c_index - key) % 26 + ord('A')
            c_og = chr(c_og_pos)
            decrypted += c_og
        elif c.islower(): 
            c_index = ord(c) - ord('a') 
            c_og_pos = (c_index - key) % 26 + ord('a')
            c_og = chr(c_og_pos)
            decrypted += c_og
        else:
            decrypted += c
    return decrypted

rot = int(input())
enc = int(input())
plain_text = input()
if enc == 0 :
    encrypted = cipher_encrypt(plain_text,rot)
    print(encrypted.lower())
else :
    decrypted = cipher_decrypt(plain_text,rot)
    print(decrypted.lower())

    