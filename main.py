# Rock, Paper, Scissors! v.1.4 (by GrobranGG) (https://github.com/GrobranGG)
import time
import os
import colorama
import sys
from colorama import Fore
from random import randint

def convert():
    colorama.init()

    opersystem = sys.platform
    clean_command = ""
    if sys.platform == "win32":
        clean_command = "cls"
    elif sys.platform == "linux":
        clean_command = "clear"
    os.system(clean_command)

    print(Fore.GREEN + " _____            _      _____                       _____      _                         ")
    print("|  __ \          | |    |  __ \                     / ____|    (_)                        ")
    print("| |__) |___   ___| | __ | |__) |_ _ _ __   ___ _ __| (___   ___ _ ___ ___  ___  _ __ ___  ")
    print("|  _  // _ \ / __| |/ / |  ___/ _` | '_ \ / _ \ '__|\___ \ / __| / __/ __|/ _ \| '__/ __| ")
    print("| | \ \ (_) | (__|   < _| |  | (_| | |_) |  __/ | _ ____) | (__| \__ \__ \ (_) | |  \__ \ ")
    print("|_|  \_\___/ \___|_|\_( )_|   \__,_| .__/ \___|_|( )_____/ \___|_|___/___/\___/|_|  |___/")
    print("                      |/           | |           |/                                      ")
    print("                                   |_|                                                   ")
    print(Fore.RED + "                                                                      v.1.4 (by GrobranGG)\n")

    print(Fore.WHITE + "Choose a language (number):")
    print("1. English")
    print("2. Russian")

    language = input(Fore.CYAN + "Enter your language: ")

    # Dictionary of all phrases in the code
    english = {'stone': 'Stone', 'scissors': 'Scissors', 'paper': 'Paper', 'youranswer': 'Your answer (number):', 'choose': 'Choose an item:',
               'choosen_stone': 'You have chosen a stone!', 'choosen_scissors': 'You have chosen scissors!', 'choosen_paper': 'You have chosen paper!',
               'computer_select': 'The computer selects the subject...', 'computer_select_stone': 'The computer chose a stone!',
               'computer_select_scissors': 'The computer chose scissors!', 'computer_select_paper': 'The computer chose paper!', 'player_won': ' You`ve won!',
               'player_lost': ' You`ve lost!', 'player_draw': ' You have a draw!', 'repeat_question': 'Choose the next action:', 'repeat_variant1': '1. Restart the program',
               'repeat_variant2': '2. Close the program', 'answer_repeat': 'Choose the answer (number): ', 'wrong choice': 'Wrong choice!'}

    russian = {'stone': 'Камень', 'scissors': 'Ножницы', 'paper': 'Бумага', 'youranswer': 'Твой ответ (число):', 'choose': 'Выбери предмет:',
               'choosen_stone': 'Ты выбрал камень!', 'choosen_scissors': 'Ты выбрал ножницы!', 'choosen_paper': 'Ты выбрал бумагу!',
               'computer_select': 'Компьютер выбирает предмет...', 'computer_select_stone': 'Компьютер выбрал камень!',
               'computer_select_scissors': 'Компьютер выбрал ножницы!', 'computer_select_paper': 'Компьютер выбрал бумагу!', 'player_won': ' Ты выиграл!',
               'player_lost': ' Ты проиграл!', 'player_draw': ' У вас ничья!', 'repeat_question': 'Выберите следующее действие:', 'repeat_variant1': '1. Перезапустить программу',
               'repeat_variant2': '2. Закрыть программу', 'answer_repeat': 'Выбери ответ (число): ', 'wrong choice': 'Неправильный выбор!'}

    if language == "1":
        lang = english
    elif language == "2":
        lang = russian
    else:
        print(Fore.RED + "Incorrect language!")
        input()
        sys.exit()

    os.system(clean_command)

    print(Fore.CYAN + lang['choose'] + "\n")
    print(Fore.RESET + "1." + lang['stone'])
    print("2." + lang['scissors'])
    print("3." + lang['paper'])
    gameobject = input(Fore.GREEN + lang['youranswer'])
    print(Fore.RESET + "\n")

    if gameobject == "1":
        os.system(clean_command)
        print(lang['choosen_stone'])
        print(lang['computer_select'])
        time.sleep(2)
        computergameobject = randint(1, 3)
        if computergameobject == 1:
            print(Fore.CYAN + lang['computer_select_stone'] + lang['player_draw'])
        elif computergameobject == 2:
            print(Fore.GREEN + lang['computer_select_scissors'] + lang['player_won'])
        elif computergameobject == 3:
            print(Fore.RED + lang['computer_select_paper'] + lang['player_lost'])

    elif gameobject == "2":
        os.system(clean_command)
        print(lang['choosen_scissors'])
        print(lang['computer_select'])
        time.sleep(2)
        computergameobject = randint(1, 3)
        if computergameobject == 1:
            print(Fore.RED + lang['computer_select_stone'] + lang['player_lost'])
        elif computergameobject == 2:
            print(Fore.CYAN + lang['computer_select_scissors'] + lang['player_draw'])
        elif computergameobject == 3:
            print(Fore.GREEN + lang['computer_select_paper'] + lang['player_won'])

    elif gameobject == "3":
        os.system(clean_command)
        print(lang['choosen_paper'])
        print(lang['computer_select'])
        time.sleep(2)
        computergameobject = randint(1, 3)
        if computergameobject == 1:
            print(Fore.GREEN + lang['computer_select_stone'] + lang['player_won'])
        elif computergameobject == 2:
            print(Fore.RED + lang['computer_select_scissors'] + lang['player_lost'])
        elif computergameobject == 3:
            print(Fore.CYAN + lang['computer_select_paper'] + lang['player_draw'])
    else:
        print(Fore.RED + lang['wrong choice'])
        sys.exit()

    print("\n")
    print(Fore.RESET + lang['repeat_question'])
    print(Fore.CYAN + lang['repeat_variant1'])
    print(lang['repeat_variant2'])
    repeat = int(input(Fore.RESET + lang['answer_repeat']))

    if repeat == 1:
        convert()
    elif repeat == 2:
        sys.exit()
    else:
        input()

convert()