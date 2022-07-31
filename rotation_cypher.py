import string
from values import *

alphabet_characters = []

user_message = input("What do you want to encrypt:")
user_list = []

input_key = input("What is your key:")
KEY = int(input_key)


for line in user_message:
    for c in line:
        user_list.append(c)


for line in ALPHABET:
    for c in line:
        alphabet_characters.append(c)




user_length = len(user_list)

deleted_chars = alphabet_characters[0:KEY]

del alphabet_characters[0:KEY]

alphabet_characters.extend(deleted_chars)

encrypted_message = alphabet_characters[0:user_length + 1]


print("This is your encrypted message")
print(encrypted_message)













