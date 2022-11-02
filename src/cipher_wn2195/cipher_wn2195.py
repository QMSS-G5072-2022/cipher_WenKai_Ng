def cipher(text, shift, encrypt=True):
    """
    This is a function that is can encrypt or decrypt a string.

    Parameters
    ----------
    text: The string the user wishes to encrypt or decrypt.
    shift: The degree wo which the text is encrpyted. For example,shift = 2 encrypts the text two letters forward.
    encypt: Boolean for whether to encrypt or decrypt. When encrypt=True, the text will be encrypted, when encrypt=False the text will be decrypted.
    
    example (encrypt):
        from cipher_wn2195 import cipher
        encrypt_text = qmss
        cipher(encrypt_tex, 3, encrypt=True)
        function returns -> tpvv
            
    example (decrypt):
        from cipher_wn2195 import cipher
        decrypt_text = tpvv
        cipher(decrypt_text, 3, encrypt=False)
        function returns -> qmss
    """
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_text = ''
    for c in text:
        index = alphabet.find(c)
        if index == -1:
            new_text += c
        else:
            new_index = index + shift if encrypt == True else index - shift
            new_index %= len(alphabet)
            new_text += alphabet[new_index:new_index+1]
    return new_text
