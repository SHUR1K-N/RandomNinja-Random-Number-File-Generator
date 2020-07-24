import time
from colorama import init
from termcolor import colored
from tqdm import tqdm
import random

correctInput = False

init()

print(colored('''

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
''', 'blue'))
print(colored('''                                    Random NumNinja: The Random Number File Generator''', 'red'))
print(colored('''                                   ---------------------------------------------------''', 'blue'))


########## Randomizer ###########

def generate(minunit, maxunit, top):

    if (progressPrompt == "1"):
        print()
        for i in tqdm(range(0, top), desc="Progress", unit=" lines", unit_scale=1):
            file.write(str(random.randrange(minunit, maxunit, 1)) + "\n")
    elif (progressPrompt == "2"):
        for i in range(0, top):
            file.write(str(random.randrange(minunit, maxunit, 1)) + "\n")
    return()


def generateUnique(minunit, maxunit, top):
    tempList = []
    while (len(tempList) < top):
        randNum = str(random.randrange(minunit, maxunit, 1)) + "\n"
        if randNum not in tempList:
            tempList.append(randNum)
            file.write(randNum)
    return()

############### Main ###############


while (correctInput is False):
    try:
        minunit = int(input("\nEnter the minimum value (Default = zero): ") or '0')
        maxunit = int(input("Enter the maximum value: "))
        top = int(input("Enter the maximum number of lines to be generated: "))

        if maxunit > minunit:
            Output = str(input("Enter output folder (Default = working folder):") or "./")
            Output += "/"

            print("\nAllow repeating values?")
            print("1. Yes\n2. No")
            uniquePrompt = input("\nSelect option number (Default = No): ") or "2"

            if uniquePrompt == "1":
                print("\nShow progress?")
                print("1. Yes (slower)\n2. No (faster)")
                progressPrompt = input("\nSelect option number (Default = No): ") or "2"

            Output += str(minunit) + " to " + str(maxunit) + " [Randomized].txt"

            maxunit += 1                        # To include the maxunit integer as well (added this far in to not interfere with file naming string)

            check = (maxunit - minunit)
            if (check >= top):
                pass
            elif (check < top):
                top = (maxunit - minunit)

            print("\nNumber of lines that will be generated: %d" % top)
            print("\nWorking...", end='')

            if uniquePrompt == "1":
                with open(Output, '+w') as file:
                    start = time.time()
                    generate(minunit, maxunit, top)
                    completionTime = time.time() - start
            elif uniquePrompt == "2":
                with open(Output, '+w') as file:
                    start = time.time()
                    generateUnique(minunit, maxunit, top)
                    completionTime = time.time() - start
            file.close()
            print("\n\nThe task completed successfully in %f seconds. (at ~%d lines/sec)" % (completionTime, top // completionTime))
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
        print("\nOne of more of the inputs are invalid. This can happen when any spaces or other characters have been entered instead of numbers. Please try again.\n")
        continue
