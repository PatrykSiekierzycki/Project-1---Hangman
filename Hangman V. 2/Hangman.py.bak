import time
from random import seed
from random import choice
import sys

#Global variable
words = ["MOM", "HELLO", "BOOK", "MONEY", "BLACK HOLE"]
miss = ""
line_as_list = []
life_points = 12

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
    while True:
        shot = input("Give me a letter: ")
        good = checking_shot(shot)
        if good == True:
            shot = shot.upper()
            return shot
            break;
        else:
            print("It is not a number! Again.")

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
        sys.exit()


"""
Brief: display user interface
Param: string type variable line
Return: None
"""
def interface(line):
    print(line)
    print(life_points)

#Losuje słowo
word = random_word()
#Ukrywa słowo
line = hide_word(word)
while True:
    interface(line)
    shot = shoting()
    line = change_line_to_list(line)
    check_shot_in_word(word)
    line = change_line_as_list_at_string(line)
    check_lose()
    check_win(line)