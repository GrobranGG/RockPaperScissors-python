import random
import time
import os
import colorama

from colorama import init
from colorama import Fore, Back
from random import randint
init()
os.system("clear")
os.system("cls")

print(Fore.GREEN + "Rock, Paper, Scissors!")
print(Fore.RED + "v.1.0 (by GrobranGG)\n")

print(Fore.WHITE + "Choose a language (number):")
print("1. English")
print("2. Russian")

print(Back.RESET)
print(Fore.CYAN)
language = input("Enter your language: ")

if language == "1":
    os.system("clear")
    os.system("cls")
    print(Fore.BLUE + "Choose an item:")
    print(Fore.RESET + "1. Stone")
    print("2. Scissors")
    print("3. Paper\n")
    gameobject = input("Your answer (number):")

    if gameobject == "1":
        print("You have chosen a stone!")
        print("The computer selects the subject...")
        time.sleep(2)
        computergameobject = randint(1, 3)
        if computergameobject == 1:
            print(Fore.GREEN + "The computer chose a stone! You have a draw!")
        elif computergameobject == 2:
            print(Fore.GREEN + "The computer chose scissors! You've won!")
        elif computergameobject == 3:
            print(Fore.GREEN + "The computer chose paper! You've lost!")

    elif gameobject == "2":
        print("You have chosen scissors!")
        print("The computer selects the subject...")
        time.sleep(2)
        computergameobject = randint(1, 3)
        if computergameobject == 1:
            print(Fore.GREEN + "The computer chose a stone! You've lost!")
        elif computergameobject == 2:
            print(Fore.GREEN + "The computer chose scissors! You have a draw!")
        elif computergameobject == 3:
            print(Fore.GREEN + "The computer chose paper! You've won!")

    elif gameobject == "3":
        print("You have chosen paper!")
        print("The computer selects the subject...")
        time.sleep(2)
        computergameobject = randint(1, 3)
        if computergameobject == 1:
            print(Fore.GREEN + "The computer chose a stone! You've won!")
        elif computergameobject == 2:
            print(Fore.GREEN + "The computer chose scissors! You've lost!")
        elif computergameobject == 3:
            print(Fore.GREEN + "The computer chose paper! You have a draw!")
    else:
        print(Fore.RED + "Wrong choice!")

elif language == "2":
    os.system("clear")
    os.system("cls")
    print(Fore.BLUE + "Выбери предмет:")
    print(Fore.RESET + "1. Камень")
    print("2. Ножницы")
    print("3. Бумага\n")
    gameobject = input("Ваш ответ (число):")

    if gameobject == "1":
        print("Вы выбрали камень!")
        print("Компьютер выбирает предмет...")
        time.sleep(2)
        computergameobject = randint(1, 3)
        if computergameobject == 1:
            print(Fore.GREEN + "Компьютер выбрал камень! У вас ничья!")
        elif computergameobject == 2:
            print(Fore.GREEN + "Компьютер выбрал ножницы! Вы выйграли!")
        elif computergameobject == 3:
            print(Fore.GREEN + "Компьютер выбрал бумагу! Вы проиграли!")

    elif gameobject == "2":
        print("Вы выбрали ножницы!")
        print("Компьютер выбирает предмет...")
        time.sleep(2)
        computergameobject = randint(1, 3)
        if computergameobject == 1:
            print(Fore.GREEN + "Компьютер выбрал камень! Вы проиграли!")
        elif computergameobject == 2:
            print(Fore.GREEN + "Компьютер выбрал ножницы! У вас ничья!")
        elif computergameobject == 3:
            print(Fore.GREEN + "Компьютер выбрал бумагу! Вы выйграли!")

    elif gameobject == "3":
        print("Вы выбрали бумагу!")
        print("Компьютер выбирает предмет...")
        time.sleep(2)
        computergameobject = randint(1, 3)
        if computergameobject == 1:
            print(Fore.GREEN + "Компьютер выбрал камень! Вы выйграли!")
        elif computergameobject == 2:
            print(Fore.GREEN + "Компьютер выбрал ножницы! Вы проиграли!")
        elif computergameobject == 3:
            print(Fore.GREEN + "Компьютер выбрал бумагу! У вас ничья!")
    else:
        print(Fore.RED + "Неверный выбор!")

else:
    print(Fore.RED + "Incorrect language!")

input()