from Script import initialization
from Script import delimiter
from Script import caesar_encryption as cae_encryp
from Script import dictionary_encryption as dic_encryp
from Script import code_break_caesar

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
            text_encryption: str = cae_encryp.encryption_decryption(text, index, "encryption")
            initialization.choice_output(text_encryption)

        elif choice_encryption == "D":
            delimiter.decryption()
            choice_decryption: str = initialization.choice_code_break_caesar(text)

            if choice_decryption == "F":
                index: int = code_break_caesar.break_caesar(text)
                text_decryption: str = cae_encryp.encryption_decryption(text, index, "encryption")
                initialization.choice_output(text_decryption)

            elif choice_decryption == "K":
                key: int = initialization.input_integer("Enter the decryption key : ")
                text_decryption: str = cae_encryp.encryption_decryption(text, key, "decryption")
                initialization.choice_output(text_decryption)

            elif choice_decryption == "B":
                text_decryption: str = code_break_caesar.brute_force(text)
                initialization.choice_output(text_decryption)

    elif choice_method == "D":
        delimiter.encryption_dictionary()
        text: str = initialization.input_choice()
        choice_encryption: str = initialization.choice_encryption_decryption()

        if choice_encryption == "C":
            delimiter.encryption()
            dict_lowerCase_uppercase: dict = {}
            file_name: str = initialization.creation_dictionary_json(dict_lowerCase_uppercase)
            text_encryption = dic_encryp.encryption_decryption(file_name, text, "encryption")
            initialization.choice_output(text_encryption)

        elif choice_encryption == "D":
            delimiter.decryption()
            file_name: str = initialization.input_character_string("Enter the name of the json dictionary : ")
            text_decryption = dic_encryp.encryption_decryption(file_name, text, "decryption")
            initialization.choice_output(text_decryption)

    delimiter.end()
