from script import initialization
from script import delimiter
from script import caesar_encryption as cae_encryp
from script import dictionary_encryption as dic_encryp
from script import code_break_caesar

if __name__ == '__main__':
    delimiter.initialization()
    choice_method: str = initialization.choice_method()

    if choice_method == "C":
        delimiter.encryption_caesar()
        text: str = initialization.input_choice()
        choice_encryption: str = initialization.choice_encryption_decryption()

        if choice_encryption == "E":
            delimiter.encryption()
            index: int = initialization.input_integer("Enter the offset index : ")
            delimiter.encryption()
            text_encryption: str = cae_encryp.encryption_decryption(text, index)
            initialization.choice_output(text_encryption)

        elif choice_encryption == "D":
            delimiter.decryption()
            choice_decryption: str = initialization.choice_code_break_caesar(text)

            if choice_decryption == "F":
                index: int = code_break_caesar.break_caesar(text)
                text_decryption: str = cae_encryp.encryption_decryption(text, index)
                initialization.choice_output(text_decryption)

            elif choice_decryption == "K":
                key: int = initialization.input_integer("Enter the decryption key : ")
                text_decryption: str = cae_encryp.encryption_decryption(text, -key)
                initialization.choice_output(text_decryption)

            elif choice_decryption == "B":
                text_decryption: str = code_break_caesar.brute_force(text)
                initialization.choice_output(text_decryption)

    elif choice_method == "D":
        delimiter.encryption_dictionary()
        text: str = initialization.input_choice()
        choice_encryption: str = initialization.choice_encryption_decryption()

        if choice_encryption == "E":
            delimiter.encryption()
            dict_lowerCase_uppercase: dict = {}
            file_name: str = initialization.creation_dictionary_json(dict_lowerCase_uppercase)
            dict_lowerCase_uppercase = initialization.open_json_dictionary(file_name)
            text_encryption = dic_encryp.encryption_decryption(text, dict_lowerCase_uppercase)
            initialization.choice_output(text_encryption)

        elif choice_encryption == "D":
            delimiter.decryption()
            file_name: str = initialization.input_character_string("Enter the name of the json dictionary : ")
            dict_lowerCase_uppercase: dict = initialization.open_json_dictionary(file_name)
            dict_lowerCase_uppercase_reverse: dict = initialization.reverse_json_dictionary(dict_lowerCase_uppercase)
            text_decryption = dic_encryp.encryption_decryption(text, dict_lowerCase_uppercase_reverse)
            initialization.choice_output(text_decryption)

    delimiter.end()
