import string
from functions import *
from values import *

user_inputstring = input("What do you want to encrypt?:")
user_inputkey = input("What is your key?:")
user_inputkey = int(user_inputkey)


indvchar_list(ALPHABET, alphabet_list)


for x in user_inputstring:
   numbers_list.append(ord(x) - 96)


for idx, el in enumerate(numbers_list):
    if el is not None:
        numbers_list[idx] += user_inputkey


user_inputstring = [alphabet_list[i] for i in numbers_list]

encrypted_string = "".join(user_inputstring)


print("This is your encrypted message:")
print(encrypted_string)

