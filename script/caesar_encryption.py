""" This is a program to encrypt with the caesar method  """

import string


def encryption_decryption(text: str, index: int):
    """

    >>> encryption_decryption('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZé', 1)
    'bcdefghijklmnopqrstuvwxyzaBCDEFGHIJKLMNOPQRSTUVWXYZAé'

    >>> encryption_decryption('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZé', 2)
    'cdefghijklmnopqrstuvwxyzabCDEFGHIJKLMNOPQRSTUVWXYZABé'

    >>> encryption_decryption('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZé', 49)
    'xyzabcdefghijklmnopqrstuvwXYZABCDEFGHIJKLMNOPQRSTUVWé'

    >>> encryption_decryption('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZé', -1)
    'zabcdefghijklmnopqrstuvwxyZABCDEFGHIJKLMNOPQRSTUVWXYé'

    >>> encryption_decryption('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZé', -2)
    'yzabcdefghijklmnopqrstuvwxYZABCDEFGHIJKLMNOPQRSTUVWXé'

    >>> encryption_decryption('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZé', -49)
    'defghijklmnopqrstuvwxyzabcDEFGHIJKLMNOPQRSTUVWXYZABCé'


    Function to encrypt or decrypt by caesar method
    :param text: Text to encrypt or decrypt
    :param index: Number of decals in alphabet
    :return: Encrypted or decrypted textb
    """
    new_text: str = ""

    for letter in text:
        nb_octet: int = ord(letter) + index
        if letter in string.ascii_lowercase:
            while nb_octet > 122:
                nb_octet = (nb_octet - 122) + 96
            while nb_octet < 97:
                nb_octet = 123 - (97 - nb_octet)
            character = chr(nb_octet)
            new_text = new_text + character

        elif letter in string.ascii_uppercase:
            while nb_octet > 90:
                nb_octet = (nb_octet - 90) + 64
            while nb_octet < 65:
                nb_octet = 91 - (65 - nb_octet)
            character = chr(nb_octet)
            new_text = new_text + character
        else:
            new_text = new_text + letter

    return new_text
