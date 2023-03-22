import json
import string
import random
import os.path


def input_character_string(answer: str):
    """
    Function to ask a question
    :param answer: Answer to the question (str)
    :return: Returns a character string
    """
    input_character: str = input(answer)
    return input_character


def input_integer(answer: int):
    """
    Function to ask a question
    :param answer: Answer to the question (int)
    :return: Returns an integer
    """
    integer: int = int(input(answer))
    return integer


def input_choice():
    """
    Function to choose the type of entry (manual or by file)
    :return: Return the function input_file or input_character_string
    """
    print("The input method?")
    print("By file (F) or manual input (M)")
    choice: chr = input("Make your choice: ")
    while choice != 'M' and choice != 'F':
        choice = input("Make your choice with M or F : ")

    if choice == 'F':
        file_name: str = input("Enter the name of the file : ")
        while True:
            if os.path.isfile("./Messages_to_encrypt/" + file_name):
                return input_file(file_name)
            else:
                file_name = input("The file does not exist! Enter another file : ")
    else:
        return input_character_string("Enter the text to be encrypted: ")


def input_file(file_name: str):
    """
    Function to read from a .txt file
    :param file_name: Name of file to read
    :return: Return only content of text file
    """
    with open("./Messages_to_encrypt/" + file_name, "r") as file:
        text: str = file.read()
    return text


def output_file(text: str):
    """
    Function to write from a .txt file
    :param text: Text to write in the file
    :return: Does not return anything but create or write a text file
    """
    file_name: str = input("Enter the output file : ")
    with open("./Messages_to_encrypt/" + file_name, "w") as file:
        file.write(text)


def choice_output(text: str):
    """
    Function to choose the type of output either by display in the terminal or in a file or both
    :param text:
    :return:
    """
    choice = input("Do you want to: display the message (D), save it to a file (S) or both (DS) ? ")
    if choice == 'S':
        output_file(text)
    elif choice == 'D':
        print("The message is : ")
        print(text)
    elif choice == 'DS' or z == 'SD':
        output_file(text)
        print("The message is : ")
        print(text)


def choice_method():
    """
    Function to select the encryption method
    :return: Returns the choice C for Caesar encryption and D for dictionary
    """
    choice: str = input("Enter the coding method Caesar (C) or Dictionary (D) : ")
    while choice != 'C' and choice != 'D':
        choice = input("Make your choice with C or D : ")

    return choice


def choice_encryption_decryption():
    """
    Function to select if you want to encrypt or decrypt
    :return: Returns the choice E for encrypt and D for decrypt
    """
    choice: str = input("Do you want to Encrypt (E) or Decrypt (D) : ")
    while choice != 'E' and choice != 'D':
        choice = input("Make your choice with E or D : ")

    return choice


def choice_code_break_caesar(text: str):
    """
    Function to select the method of breaking the Caesar code: by frequency of appearance, by brute force or by the
    decryption key :param text: Number of characters in the text because a minimum for the frequency of appearance
    :return: Returns the choice F for frequency of appearance, B for brute force and K for the decryption key
    """
    nb_character = len(text)
    choice: str = input("Do you want to: break the cesar code by brute force (B), by frequency of appearance of the "
                        "letters (F) or with the decryption key (K) ? ")
    while choice != 'B' and choice != 'F' and choice != 'K':
        choice = input("Choose between B, F, K : ")

    if nb_character < 185 and choice == 'F':
        print("The text to be decrypted does not contain enough characters to break the cesar code by frequency of "
              "occurrence")
        while choice != 'B' and choice != 'K':
            choice = input("Choose between B, K : ")
    return choice


def creation_dictionary_json(dict_lowerCase_uppercase: dict):
    """
    Function to create the dictionary allowing dictionary coding
    :param dict_lowerCase_uppercase: Empty dictionary which will take the encryption key
    :return: Returns the created dictionary name
    """
    list_lowercase_uppercase: list = list(string.ascii_lowercase + string.ascii_uppercase)
    list_lowercase_uppercase_shuffle: list = list_lowercase_uppercase.copy()

    random.shuffle(list_lowercase_uppercase_shuffle)

    for i in range(52):
        dict_lowerCase_uppercase[list_lowercase_uppercase[i]] = list_lowercase_uppercase_shuffle[i]

    file_name: str = input("Enter the name of the json dictionary : ")
    with open("./Messages_to_encrypt/" + file_name + ".json", "w") as dictionary:
        json.dump(dict_lowerCase_uppercase, dictionary)

    return file_name


def open_json_dictionary(file_name: str):
    with open("./Messages_to_encrypt/" + file_name + ".json", "r") as dictionary:
        dict_lowercase: dict = json.load(dictionary)

    return dict_lowercase


def reverse_json_dictionary(dict_original: dict):
    dict_reverse: dict = {}
    for key, value in dict_original.items():
        dict_reverse[value] = key

    return dict_reverse
