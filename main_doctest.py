""" Program to perform doctest on ceasar and dictionary encryption methods """
import doctest
from script import caesar_encryption
from script import dictionary_encryption

if __name__ == '__main__':
    doctest.testmod(caesar_encryption, verbose=True)
    doctest.testmod(dictionary_encryption, verbose=True)
