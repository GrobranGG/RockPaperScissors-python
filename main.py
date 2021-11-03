# Rock, Paper, Scissors! v.1.1 (by GrobranGG) (https://github.com/GrobranGG)
import random
import time
import os
import colorama
import sys

opersystem = sys.platform
from colorama import Fore, Back
from random import randint
colorama.init()

if opersystem == "win32":
    os.system("cls")
elif opersystem == 'linux':
    os.system("clear")

print(Fore.GREEN + "Rock, Paper, Scissors!")
print(Fore.RED + "v.1.1 (by GrobranGG)\n")

print(Fore.WHITE + "Choose a language (number):")
print("1. English")
print("2. Russian")

print(Fore.CYAN)
language = input("Enter your language: ")

# Dictionary of all phrases in the code
english = {'stone': 'Stone', 'scissors': 'Scissors', 'paper': 'Paper', 'youranswer': 'Your answer (number):', 'choose': 'Choose an item:',
           'choosen_stone': 'You have chosen a stone!', 'choosen_scissors': 'You have chosen scissors!', 'choosen_paper': 'You have chosen paper!',
           'computer_select': 'The computer selects the subject...', 'computer_select_stone': 'The computer chose a stone!',
           'computer_select_scissors': 'The computer chose scissors!', 'computer_select_paper': 'The computer chose paper!', 'player_won': ' You`ve won!',
           'player_lost': ' You`ve lost!', 'player_draw': ' You have a draw!'}

russian = {'stone': 'Камень', 'scissors': 'Ножницы', 'paper': 'Бумага', 'youranswer': 'Твой ответ (число):', 'choose': 'Выбери предмет:',
           'choosen_stone': 'Ты выбрал камень!', 'choosen_scissors': 'Ты выбрал ножницы!', 'choosen_paper': 'Ты выбрал бумагу!',
           'computer_select': 'Компьютер выбирает предмет...', 'computer_select_stone': 'Компьютер выбрал камень!',
           'computer_select_scissors': 'Компьютер выбрал ножницы!', 'computer_select_paper': 'Компьютер выбрал бумагу!', 'player_won': ' Ты выиграл!',
           'player_lost': ' Ты проиграл!', 'player_draw': ' У вас ничья!'}

if language == "1":
    lang = english
elif language == "2":
    lang = russian
else:
    print(Fore.RED + "Incorrect language!")
    input()
    sys.exit()

print(Back.RESET)

if opersystem == "win32":
    os.system("cls")
elif opersystem == 'linux':
    os.system("clear")

print(Fore.BLUE + lang['choose'])
print(Fore.RESET + "1." + lang['stone'])
print("2." + lang['scissors'])
print("3." + lang['paper'] + "\n")
gameobject = input(lang['youranswer'])
if gameobject == "1":
    print(lang['choosen_stone'])
    print(lang['computer_select'])
    time.sleep(2)
    computergameobject = randint(1, 3)
    if computergameobject == 1:
        print(Fore.GREEN + lang['computer_select_stone'] + lang['player_draw'])
    elif computergameobject == 2:
        print(Fore.GREEN + lang['computer_select_scissors'] + lang['player_won'])
    elif computergameobject == 3:
        print(Fore.GREEN + lang['computer_select_paper'] + lang['player_lost'])

elif gameobject == "2":
    print(lang['choosen_scissors'])
    print(lang['computer_select'])
    time.sleep(2)
    computergameobject = randint(1, 3)
    if computergameobject == 1:
        print(Fore.GREEN + lang['computer_select_stone'] + lang['player_lost'])
    elif computergameobject == 2:
        print(Fore.GREEN + lang['computer_select_scissors'] + lang['player_draw'])
    elif computergameobject == 3:
        print(Fore.GREEN + lang['computer_select_paper'] + lang['player_won'])

elif gameobject == "3":
    print(lang['choosen_paper'])
    print(lang['computer_select'])
    time.sleep(2)
    computergameobject = randint(1, 3)
    if computergameobject == 1:
        print(Fore.GREEN + lang['computer_select_stone'] + lang['player_won'])
    elif computergameobject == 2:
        print(Fore.GREEN + lang['computer_select_scissors'] + lang['player_lost'])
    elif computergameobject == 3:
        print(Fore.GREEN + lang['computer_select_paper'] + lang['player_draw'])
else:
    print(Fore.RED + "Wrong choice!")
    input()
    sys.exit()

input()