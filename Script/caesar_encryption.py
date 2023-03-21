""" This is a program to encrypt with the caesar method  """

import string


def encryption_decryption(text: str, index: int, mode: str):
    """
    Function to encrypt or decrypt by caesar method
    :param text: Text to encrypt or decrypt
    :param index: Number of decals in alphabet
    :param mode: Choose between encrypt or decrypt
    :return: Encrypted or decrypted text
    """
    new_text: str = ""
    nb_octet: int = 0

    for letter in text:

        if mode == "encryption":
            nb_octet = ord(letter) + index
        if mode == "decryption":
            nb_octet = ord(letter) - index

        if letter in string.ascii_lowercase:
            while nb_octet > 122:
                nb_octet = ((nb_octet - 122) + 96)
            while nb_octet < 97:
                nb_octet = (123 - (97 - nb_octet))
            character: str = chr(nb_octet)
            new_text = new_text + character

        elif letter in string.ascii_uppercase:
            while nb_octet > 90:
                nb_octet = ((nb_octet - 90) + 64)
            while nb_octet < 65:
                nb_octet = (91 - (65 - nb_octet))
            character: str = chr(nb_octet)
            new_text = new_text + character
        else:
            new_text = new_text + letter

    return new_text

