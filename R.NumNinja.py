import time
from colorama import init
from termcolor import colored
from tqdm import tqdm
import random

correctInput = False

BANNER1 = colored('''

             ██▀███        ███▄    █  █    ██  ███▄ ▄███▓ ███▄    █  ██▓ ███▄    █  ▄▄▄██▀▀▀▄▄▄
            ▓██ ▒ ██▒      ██ ▀█   █  ██  ▓██▒▓██▒▀█▀ ██▒ ██ ▀█   █ ▓██▒ ██ ▀█   █    ▒██  ▒████▄
            ▓██ ░▄█ ▒     ▓██  ▀█ ██▒▓██  ▒██░▓██    ▓██░▓██  ▀█ ██▒▒██▒▓██  ▀█ ██▒   ░██  ▒██  ▀█▄
            ▒██▀▀█▄       ▓██▒  ▐▌██▒▓▓█  ░██░▒██    ▒██ ▓██▒  ▐▌██▒░██░▓██▒  ▐▌██▒▓██▄██▓ ░██▄▄▄▄██
            ░██▓ ▒██▒ ██▓ ▒██░   ▓██░▒▒█████▓ ▒██▒   ░██▒▒██░   ▓██░░██░▒██░   ▓██░ ▓███▒   ▓█   ▓██▒
            ░ ▒▓ ░▒▓░ ▒▓▒ ░ ▒░   ▒ ▒ ░▒▓▒ ▒ ▒ ░ ▒░   ░  ░░ ▒░   ▒ ▒ ░▓  ░ ▒░   ▒ ▒  ▒▓▒▒░   ▒▒   ▓▒█░
              ░▒ ░ ▒░ ░▒  ░ ░░   ░ ▒░░░▒░ ░ ░ ░  ░      ░░ ░░   ░ ▒░ ▒ ░░ ░░   ░ ▒░ ▒ ░▒░    ▒   ▒▒ ░
              ░░   ░  ░      ░   ░ ░  ░░░ ░ ░ ░      ░      ░   ░ ░  ▒ ░   ░   ░ ░  ░ ░ ░    ░   ▒
               ░       ░           ░    ░            ░            ░  ░           ░  ░   ░        ░  ░
                       ░
''', 'blue')
BANNER2 = colored('''                                Random NumNinja: The Random Number File Generator''', 'red')
BANNER3 = colored('''                               ---------------------------------------------------''', 'blue')
numSet = set()


def printBanner():
    init()
    print(BANNER1), print(BANNER2), print(BANNER3)

########## Randomizer ###########


def generate():

    if (progressPrompt == 1):
        print()
        for i in tqdm(range(0, top), desc="Progress", unit=" lines", unit_scale=1):
            file.write(str(random.randrange(minunit, maxunit + 1, 1)) + "\n")
    elif (progressPrompt == 2):
        for i in range(0, top):
            file.write(str(random.randrange(minunit, maxunit + 1, 1)) + "\n")


def generateUnique():
    while (len(numSet) <= top):
        randNum = str(random.randrange(minunit, maxunit + 1, 1))
        numSet.add(randNum)
    for element in numSet:
        file.write(element + "\n")


############### Main ###############

if __name__ == "__main__":

    printBanner()

    while (correctInput is False):
        try:
            minunit = int(input("\nEnter the minimum value (Default = zero): ") or 0)
            maxunit = int(input("Enter the maximum value: "))

            if maxunit > minunit:
                Output = str(input("Enter output folder (Default = working folder):") or "./")
                Output += "/"

                print("\nAllow repeating values?")
                print("1. Yes\n2. No")
                uniquePrompt = int(input("\nSelect option number (Default = No): ") or 2)

                if (uniquePrompt == 1):
                    print("\nShow progress?")
                    print("1. Yes (slower)\n2. No (faster)")
                    progressPrompt = int(input("\nSelect option number (Default = No): ") or 2)

                Output += f"{minunit} to {maxunit} [Randomized].txt"

                top = int(input("\nEnter the maximum number of lines to be generated (Default = maximum within specified limit): ") or (maxunit - minunit))

                checkTop = (maxunit - minunit)
                if (checkTop >= top):
                    pass
                elif (checkTop < top):
                    top = (maxunit - minunit)

                print(f"\nNumber of lines that will be generated: {top + 1}")
                print("\nWorking...", end='')

                if (uniquePrompt == 1):
                    with open(Output, "w") as file:
                        start = time.time()
                        generate()
                        completionTime = time.time() - start
                elif (uniquePrompt == 2):
                    with open(Output, "w") as file:
                        start = time.time()
                        generateUnique()
                        completionTime = time.time() - start
                rate = top // completionTime

                print(f"\n\nThe task completed successfully in {completionTime} seconds. (at ~{rate} lines/sec)")
                print("Press any key to exit.")
                input()

                break

            elif (minunit == maxunit):
                print("\nThe minimum value cannot be equal to the maximum value.")

            elif (minunit > maxunit):
                print("\nThe minimum value cannot be greater than the maximum value.")
        except ZeroDivisionError:
            print("\n\nThe task completed successfully in zero seconds.")
            print("Press any key to exit.")
            input()
            break
        except:
            print(e)
            print("\nOne of more of the inputs are invalid. This can happen when any spaces or other characters have been entered instead of numbers. Please try again.\n")
            continue
        correctInput = True
