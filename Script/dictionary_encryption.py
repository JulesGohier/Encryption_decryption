import string
import json


def encryption_decryption(file_name: str, text: str, mode: str):
    """
    Function to encrypt or decrypt by dictionary
    :param file_name: Dictionary  name to encrypt or decrypt
    :param text: Text to encrypt or decrypt
    :param mode: Choose between encrypt or decrypt
    :return: Encrypted or decrypted text
    """
    new_text: str = ""
    for letter in text:
        value: str = ""
        if mode == 'encryption':
            with open("./Messages_to_encrypt/" + file_name + ".json", "r") as dictionary:
                dict_lowercase: dict = json.load(dictionary)
                value = dict_lowercase.get(letter)
        elif mode == 'decryption':
            with open("./Messages_to_encrypt/" + file_name + ".json", "r") as dictionary:
                dict_original: dict = json.load(dictionary)
                dict_reverse = {}
                for key, value in dict_original.items():
                    dict_reverse[value] = key
                value = dict_reverse.get(letter)

        if letter in string.ascii_lowercase:
            new_text = new_text + value

        elif letter in string.ascii_uppercase:
            new_text = new_text + value
        else:
            new_text = new_text + letter

    return new_text
