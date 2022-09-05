import time
from random import seed
from random import choice
import os
import sys


#Global variable
words = ["MOM", "HELLO", "BOOK", "MONEY", "BLACK HOLE"]
miss = ""
line_as_list = []
life_points = 12
miss_as_list = []
clean = True
inter = True

"""
Brief: Print another hangman part reley to life_points value
Param: None
Return: None
"""
def print_hangman():

    global life_points

    if life_points == 12:
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print("__________________________________________________________")
    if life_points == 11:
        print()
        print()
        print()
        print()
        print()
        print("    /")
        print("   /")
        print("__/____________________________")
    if life_points == 10:
        print()
        print()
        print()
        print()
        print()
        print("    /|")
        print("   / |")
        print("__/__|_________________________")
    if life_points == 9:
        print()
        print()
        print()
        print()
        print()
        print("    /|\ ")
        print("   / | \ ")
        print("__/__|__\______________________")
    if life_points == 8:
        print("     |")
        print("     |")
        print("     |")
        print("     |")
        print("     |")
        print("    /|\ ")
        print("   / | \ ")
        print("__/__|__\______________________")
    if life_points == 7:
        print("     |--------------")
        print("     |")
        print("     |")
        print("     |")
        print("     |")
        print("    /|\ ")
        print("   / | \ ")
        print("__/__|__\______________________")
    if life_points == 6:
        print("     |--------------")
        print("     |          |")
        print("     |")
        print("     |")
        print("     |")
        print("    /|\ ")
        print("   / | \ ")
        print("__/__|__\______________________")
    if life_points == 5:
        print("     |--------------")
        print("     |          |")
        print("     |        (x;x)")
        print("     |")
        print("     |")
        print("    /|\ ")
        print("   / | \ ")
        print("__/__|__\______________________")
    if life_points == 4:
        print("     |--------------")
        print("     |          |")
        print("     |        (x;x) ")
        print("     |          |")
        print("     |          |")
        print("    /|\ ")
        print("   / | \ ")
        print("__/__|__\______________________")
    if life_points == 3:
        print("     |--------------")
        print("     |          |")
        print("     |        (x;x) ")
        print("     |          |\ ")
        print("     |          | \ ")
        print("    /|\   ")
        print("   / | \  ")
        print("__/__|__\______________________")
    if life_points == 2:
        print("     |--------------")
        print("     |          |")
        print("     |        (x;x) ")
        print("     |         /|\ ")
        print("     |        / | \ ")
        print("    /|\   ")
        print("   / | \      ")
        print("__/__|__\______________________")
    if life_points == 1:
        print("     |--------------")
        print("     |          |")
        print("     |        (x;x) ")
        print("     |         /|\ ")
        print("     |        / | \ ")
        print("    /|\        /")
        print("   / | \      /")
        print("__/__|__\______________________")
    if life_points == 0:
        print("     |--------------")
        print("     |          |")
        print("     |        (x;x) ")
        print("     |         /|\ ")
        print("     |        / | \ ")
        print("    /|\        / \ ")
        print("   / | \      /   \ ")
        print("__/__|__\______________________")


"""
Brief: random chose the word from words list
Param: None
Return: word - string variable with chosen word from list words
"""

def random_word():

    seed(time.time())
    global words
    word = choice(words)
    return word

"""
Brief: Creat new string, based on variable word, where ech letter is changed into " " except spacebar chars
Param: variable word
Return: string type variable line
"""

def hide_word(word):

    line = ""

    for letter in word:
        if letter.isalpha() == True:
            line = line + "_"
        elif letter == " ":
            line = line + " "

    return line

"""
Brief: Get char from user and call function checking_shot if checking_shot return true shot is change for capital letter and returned. If checking_shot return false  program again please user to give a letter untill user give a letter
Param: None
Return: shot - char type variable with users letter changing to capital letter
"""
def shoting():

    global word, life_points, clean, inter
    next = False

    while True:

        if clean == True:
            clean_console()
            clean = True

        if inter == True:
            interface(line)
            inter = True

        shot = input("Give me a letter: ")
        good = checking_shot(shot)
        next = guess_all(shot, word)
        if good == True and next == True:
            shot = shot.upper()
            inter = True
            return shot
            break;
        elif next == True:
            clean_console()
            interface(line)
            print("It is not a letter! Again.")
            clean = False
            inter = False
        next = False

"""
Brief: check that the user give the code to try guess all quiz, if not check how much user give a letter if more than one print error
Param: char type variable shot, string word
Return: None
"""
def guess_all(shot, word):

    global miss, life_points, inter, clean

    if shot == "guess":
        guess_shot = input("Try to guess the phrase: ")
        guess_shot = guess_shot.upper()
        if guess_shot == word and guess_shot.isalpha():
            print("You win! Congratulation!")
            sys.exit()
        elif guess_shot != word and guess_shot.isalpha():
            life_points = life_points - 1
            add_to_miss(guess_shot)
            clean_console()
            interface(line)
            print("It is not a phrase to guess")
            inter = False
            clean = False
            return False
        elif guess_shot.isalpha() == False:
            clean_console()
            interface(line)
            print("It is not a letter!")
            clean = False
            inter = False
            return False
    else:
        count = len(shot)
        if count != 1:

            clean_console()
            interface(line)
            print("Wrong input")
            clean = False
            inter = False
        else:
            return True


"""
Brief: checking that, the users shot is a letter. If shot is a letter return True, if not return False
Param: shot
Return True/False
"""
def checking_shot(shot):
    good = shot.isalpha()

    if good == True:
        return True
    else:
        return False

"""
Brief: change string type variable line into list
Param: string variable line
Return: None
"""
def change_line_to_list(line):

    global line_as_list

    line_as_list.clear()

    for sign in line:
        line_as_list.append(sign)

    line = ""
    return line

"""
Brief: check is variable shot in string variable word if is put variable shot in adequate place in list type variable line_as_list. If it is not in variable word subtract z
a one point from int variable life_points
Param: string type variable word
Return: None
"""
def check_shot_in_word(word):

    global life_points
    flag = False

    for index, sign in enumerate(word):
        if sign == shot:
            line_as_list[index] = sign
            flag = True

    if flag == False:
        life_points = life_points - 1
        add_to_miss(shot)

    #Clean flag
    flag = False

"""
Brief: change list type variable line_as_list to string line and return line, after return the string variable line is overwrite by that returning value
Param: string type variable line
Return: string variable line
"""
def change_line_as_list_at_string(line):

    global line_as_list


    for sign in line_as_list:
        line = line + sign

    return line

"""
Brief: check the game status. If life_points are equal zero then print information about lose game and finish program
Param: None
Return: None
"""
def check_lose():

    global life_points

    if life_points == 0:
        print("You lose!")
        input()
        sys.exit()


"""
Brief: check game status. if variable line is equal to word, print info about win and finish program
Param: string type variable line
Return: None
"""
def check_win(line):

    global word

    if line == word:
        print("You win! Congratulation!")
        input()
        sys.exit()


"""
Brief: display user interface
Param: string type variable line
Return: None
"""
def interface(line):

        print_hangman()
        print()
        print()
        print(line)
        print()
        print()
        print("Life: ", life_points)
        print(miss)


"""
Brief: Clear console
Param: None
Return: None
"""
def clean_console():

    os.system('cls')


"""
Brief: Add to string miss new users miss input, and if miss was before don't add that miss again
Param: char type variable shot
Return: None
"""
def add_to_miss(shot):

    global miss

    flag = False

    change_miss_to_list()
    for sign in miss_as_list:
        if sign == shot:
            flag = True

    if flag == False:
        miss = miss + shot + " "

    flag == False
    clean_table_with_miss()

"""
Brief: Take string variable and on it's base make a new table miss_as_list
Param: None
Return: None 
"""
def change_miss_to_list():

    global miss, miss_as_list

    miss_as_list = miss.split()

"""
Brief: Clean tabel miss_ass_list
Param: None
Return: None
"""
def clean_table_with_miss():
    global miss_as_list

    miss_as_list.clear()


#Losuje słowo
word = random_word()
#Ukrywa słowo
line = hide_word(word)
while True:
    shot = shoting()
    line = change_line_to_list(line)
    check_shot_in_word(word)
    line = change_line_as_list_at_string(line)
    check_lose()
    check_win(line)
    clean_console()