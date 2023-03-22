""" This is an encryption program with the dictionary method """
import string


def encryption_decryption(text: str, dict_lowercase: dict):
    """
    >>> dictonary: dict = {"a": "g", "b": "v", "c": "f", "d": "O", "e": "A", "f": "H", "g": "S", "h": "b", "i": "C", "j": "h", "k": "N", "l": "U", "m": "L", "n": "e", "o": "w", "p": "n", "q": "t", "r": "K", "s": "Z", "t": "E", "u": "i", "v": "j", "w": "Y", "x": "B", "y": "l", "z": "u", "A": "W", "B": "r", "C": "m", "D": "c", "E": "I", "F": "V", "G": "z", "H": "k", "I": "p", "J": "D", "K": "y", "L": "R", "M": "o", "N": "P", "O": "G", "P": "T", "Q": "J", "R": "q", "S": "s", "T": "X", "U": "a", "V": "x", "W": "Q", "X": "M", "Y": "F", "Z": "d"}

    >>> encryption_decryption('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZé', dictonary)
    'gvfOAHSbChNULewntKZEijYBluWrmcIVzkpDyRoPGTJqsXaxQMFdé'


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
