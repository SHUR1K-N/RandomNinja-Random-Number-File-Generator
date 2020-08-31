import time; import os
from colorama import init
from termcolor import colored
from tqdm import tqdm
import random

BANNER1 = colored('''

         ██▀███   ▄▄▄       ███▄    █ ▓█████▄  ▒█████   ███▄ ▄███▓ ███▄    █  ██▓ ███▄    █  ▄▄▄██▀▀▀▄▄▄
        ▓██ ▒ ██▒▒████▄     ██ ▀█   █ ▒██▀ ██▌▒██▒  ██▒▓██▒▀█▀ ██▒ ██ ▀█   █ ▓██▒ ██ ▀█   █    ▒██  ▒████▄
        ▓██ ░▄█ ▒▒██  ▀█▄  ▓██  ▀█ ██▒░██   █▌▒██░  ██▒▓██    ▓██░▓██  ▀█ ██▒▒██▒▓██  ▀█ ██▒   ░██  ▒██  ▀█▄
        ▒██▀▀█▄  ░██▄▄▄▄██ ▓██▒  ▐▌██▒░▓█▄   ▌▒██   ██░▒██    ▒██ ▓██▒  ▐▌██▒░██░▓██▒  ▐▌██▒▓██▄██▓ ░██▄▄▄▄██
        ░██▓ ▒██▒ ▓█   ▓██▒▒██░   ▓██░░▒████▓ ░ ████▓▒░▒██▒   ░██▒▒██░   ▓██░░██░▒██░   ▓██░ ▓███▒   ▓█   ▓██▒
        ░ ▒▓ ░▒▓░ ▒▒   ▓▒█░░ ▒░   ▒ ▒  ▒▒▓  ▒ ░ ▒░▒░▒░ ░ ▒░   ░  ░░ ▒░   ▒ ▒ ░▓  ░ ▒░   ▒ ▒  ▒▓▒▒░   ▒▒   ▓▒█░
          ░▒ ░ ▒░  ▒   ▒▒ ░░ ░░   ░ ▒░ ░ ▒  ▒   ░ ▒ ▒░ ░  ░      ░░ ░░   ░ ▒░ ▒ ░░ ░░   ░ ▒░ ▒ ░▒░    ▒   ▒▒ ░
          ░░   ░   ░   ▒      ░   ░ ░  ░ ░  ░ ░ ░ ░ ▒  ░      ░      ░   ░ ░  ▒ ░   ░   ░ ░  ░ ░ ░    ░   ▒
           ░           ░  ░         ░    ░        ░ ░         ░            ░  ░           ░  ░   ░        ░  ░
           ''', 'blue')
BANNER2 = colored('''                                   RandomNinja: The Random Number File Generator''', 'red')
BANNER3 = colored('''                                   ---------------------------------------------''', 'blue')
numSet = set()


def printBanner():
    init()
    print(BANNER1), print(BANNER2), print(BANNER3)

########## Randomizer ###########


def generate():

    if (progressPrompt == "1"):
        print()
        for i in tqdm(range(0, top), desc="Progress", unit=" lines", unit_scale=1):
            file.write(str(random.randrange(minunit, maxunit + 1, 1)) + "\n")
    elif (progressPrompt == "2"):
        for i in range(0, top):
            file.write(str(random.randrange(minunit, maxunit + 1, 1)) + "\n")


def generateUnique():
    while (len(numSet) <= top):
        randNum = str(random.randrange(minunit, maxunit + 1, 1))
        numSet.add(randNum)
    for element in numSet:
        file.write(element + "\n")


def clrscr():
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        _ = os.system('cls')
    printBanner()


############### Main ###############

if __name__ == "__main__":

    printBanner()

    while (True):
        try:
            minunit = int(input("\nEnter the minimum value (Default = zero): ") or 0)
            maxunit = int(input("Enter the maximum value: "))
            break

            if (maxunit > minunit):
                pass
            elif (minunit == maxunit):
                clrscr()
                print("\nThe minimum value cannot be equal to the maximum value.")
                continue

            elif (minunit > maxunit):
                clrscr()
                print("\nThe minimum value cannot be greater than the maximum value.")
                continue
        except:
            clrscr()
            print("\nInvalid entry (not an integer). Please try again.\n")
            continue

    while (True):
        print("\nAllow repeating values?")
        print("1. Yes\n2. No")
        uniquePrompt = input("\nSelect option number (Default = No): ") or "2"

        if (uniquePrompt == "1"):
            print("\nShow progress?")
            print("1. Yes (slower)\n2. No (faster)")
            progressPrompt = input("\nSelect option number (Default = No): ") or "2"
            break

        elif (uniquePrompt == "2"):
            break

        else:
            clrscr()
            print("\nInvalid entry. Choose either option 1 or 2. Try again.\n")
            continue

    while (True):
        try:
            top = int(input("\nEnter the maximum number of lines to be generated (Default = maximum within specified limit): ") or (maxunit - minunit))
            break
        except:
            clrscr()
            print("\nInvalid entry (not an integer). Please try again.\n")
            continue

    while (True):
        output = str(input("\nEnter output folder (Default = working folder):") or "./")
        output += "/"

        if (os.path.exists(output) is True):
            output += f"{minunit} to {maxunit} [Randomized].txt"
            break
        else:
            clrscr()
            print("\nEither file does not exist or invalid path entered. Try again.\n")
            continue

    checkTop = (maxunit - minunit)
    if (checkTop >= top):
        pass
    elif (checkTop < top):
        top = (maxunit - minunit)

    clrscr()
    print(f"\nNumber of lines that will be generated: {top + 1}")
    print("\nWorking...", end='')

    if (uniquePrompt == "1"):
        with open(output, "w") as file:
            start = time.time()
            generate()
            completionTime = time.time() - start
    elif (uniquePrompt == "2"):
        with open(output, "w") as file:
            start = time.time()
            generateUnique()
            completionTime = time.time() - start
    try:
        rate = top // completionTime

        clrscr()
        print(f"\n\nThe task completed successfully in {completionTime} seconds. (at ~{rate} lines/sec)")
        print("Press Enter to exit.")
        input()

    except ZeroDivisionError:
        clrscr()
        print("\n\nThe task completed successfully in zero seconds.")
        print("Press Enter to exit.")
        input()
