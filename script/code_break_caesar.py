""" This is a program to break the caesar code """

import string
from script import french_dictionary
from script import caesar_encryption


def break_caesar(text: str):
    """
    Function to break the caesar code by caesar method
    :param text: Decrypted text
    :return: Encrypted text
    """
    list_lowercase_uppercase: list = list(
        string.ascii_lowercase + string.ascii_uppercase
    )
    dict_lowercase_uppercase = {}
    nb_lowercase_uppercase: int = len(list_lowercase_uppercase)
    for letter in range(nb_lowercase_uppercase):
        dict_lowercase_uppercase[list_lowercase_uppercase[letter]] = 0

    for letter in text:
        if letter in list_lowercase_uppercase:
            dict_lowercase_uppercase[letter] = dict_lowercase_uppercase.get(letter) + 1

    dict_lowercase_uppercase_sort = dict(
        sorted(dict_lowercase_uppercase.items(), key=lambda x: x[1], reverse=True)
    )

    list_lowercase_uppercase_alphabet = list(dict_lowercase_uppercase_sort)

    number_byte1: int = ord(list_lowercase_uppercase_alphabet[0])
    number_byte1 = ord("e") - number_byte1

    number_byte2: int = ord(list_lowercase_uppercase_alphabet[1])
    number_byte2 = ord("a") - number_byte2

    number_byte: int = int((number_byte1 + number_byte2) / 2)

    return number_byte


def brute_force(text: str):
    """
    Function to attack the encrypted message by brute force and compare
    with a dictionary of French words
    :param text: Encrypted text to attack
    :return: All possibility clues between 1 and 26, with sentence and index
    """
    dictionary_text: dict = {}
    for key in range(1, 26):
        nb_check: int = 0

        text_decryption: str = caesar_encryption.encryption_decryption(text, key)
        text_decryption_list: list = text_decryption.split(" ")
        nb_text_decryption_list = len(text_decryption_list)
        for words in range(nb_text_decryption_list):
            if text_decryption_list[words] in french_dictionary.dictionary:
                nb_check = nb_check + 1

        text_key: str = text_decryption + " -> " + str(key) + " or " + str(-key)
        text_value: str = str(nb_check)
        dictionary_text[text_key] = text_value

    dictionary_text_sort: dict = dict(
        sorted(dictionary_text.items(), key=lambda x: x[1], reverse=True)
    )
    text_output: list = list(dictionary_text_sort)

    return text_output[0]
