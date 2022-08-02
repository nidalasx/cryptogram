
#Testing main menu

from simple_term_menu import TerminalMenu


#Menu options

options = ["[1] Encrypt", "[2] Decrypt", "[q] Quit"]


mainMenu = TerminalMenu(options, title = "Encryptor")

#Creates submenu if user presses "encrypt"
submenu_encrypt = TerminalMenu(["[1] Caesar", "[2] Coming soon", "[q] Quit"], title = "Encrypt")

quitting = False



while quitting == False:
    options_index = mainMenu.show()
    options_choice = options[options_index]

    if(options_choice == "[q] Quit"):
        quitting = True
    if(options_choice == "[1] Encrypt"):
        submenu_encrypt.show()
    else: 
        print(options_choice)









