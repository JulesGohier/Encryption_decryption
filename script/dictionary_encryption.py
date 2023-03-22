import string
import json


def encryption_decryption(text: str, dict_lowercase: dict):
    """
    Function to encrypt or decrypt by dictionary
    :param dict_lowercase:
    :param text: Text to encrypt or decrypt
    :return: Encrypted or decrypted text
    """
    new_text: str = ""
    for letter in text:
        value: str = dict_lowercase.get(letter)

        if letter in string.ascii_lowercase:
            new_text = new_text + value

        elif letter in string.ascii_uppercase:
            new_text = new_text + value
        else:
            new_text = new_text + letter

    return new_text
