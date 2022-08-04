from values import *
import string

#Global variables
plain_text = None
key = None 



#Asks the users for their message and their key

def input_start():
    
    
    #Users message

    global plain_text
    plain_text = input("What text do you want to encrypt?: ")
    
    #Users key

    global key
    key = input("What key?: ")
    key = int(key)
    
    return plain_text, key

input_start()


#Shifts and replaces the alphabets according to the desired key

def caesar(text, shift, alphabets):

    def shift_alphabet(alphabet):
        return alphabet[shift:] + alphabet[:shift]

    shifted_alphabets = tuple(map(shift_alphabet, alphabets))
    final_alphabet = "".join(alphabets)
    final_shifted_alphabet = "".join(shifted_alphabets)
    table = str.maketrans(final_alphabet, final_shifted_alphabet)
    return text.translate(table)


#Prints the encrypted message

print(caesar(plain_text, key, [string.ascii_lowercase, string. ascii_uppercase, string.punctuation]))