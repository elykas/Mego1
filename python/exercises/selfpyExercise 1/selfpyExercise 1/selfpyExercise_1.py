 
HANGMAN_ASCII_ART="""Welcome to the game Hangman
    _    _
   | |  | |
   | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
   |  __  |/ _' | '_ \ / _' | '_ ' _ \ / _' | '_ \\
   | |  | | (_| | | | | (_| | | | | | | (_| | | | |
   |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                        __/ |
                       |___/
                       """
def is_valid_input(user_letter):
    if(len(user_letter)!=1):
        return False
    if(ord(user_letter)<ord('a') and ord(user_letter)>ord('z')\
     and ord(user_letter) < ord('A') and ord(user_letter)>ord('Z')):
        return False
    else:
        return True

MAX_TRIES=6 
guessing_a_letter=input("Please enter a word: ")
print(guessing_a_letter)
guess_word="_ "*len(guessing_a_letter)
print(guess_word)
user_letter=input("Please guess a letter :")
print(is_valid_input(user_letter))
    