import string

from rx import return_value
from values import *
from functions import *


user_message = input("What do you want to encrypt:")


input_key = input("What is your key:")
KEY = int(input_key)



indvchar_list(ALPHABET, alphabet_characters)
indvchar_list(user_message, user_list)

user_length = len(user_list)

deleted_chars = alphabet_characters[0:KEY]

del alphabet_characters[0:KEY]

alphabet_characters.extend(deleted_chars)

encrypted_message = alphabet_characters[0:user_length]


print("This is your encrypted message")
print(encrypted_message)













