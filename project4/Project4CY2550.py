#!/usr/bin/env python3
import sys
import random

listOfWords = open("words.txt").read().split()
symbols = "~!@#$%^&*.:;"

def generatePassword(numWords, numCaps, numNumbers, numSymbols):
    words = []
    for i in range(numWords):
        words.append(random.choice(listOfWords).lower())
    for i in range(numCaps):
        words[i] = words[i].title()
    for i in range(numNumbers):
        words.append(random.randint(0, 9))
    for i in range(numSymbols):
        words.append(random.choice(symbols))
    random.shuffle(words)
    password = ""
    for i in words:
        password = password + str(i)
    return password

if __name__ == "__main__":
    doGeneration = True
    numWords = 4
    numCaps = 0
    numNumbers = 0
    numSymbols = 0
    for i, arg in enumerate(sys.argv):
        if(arg == "-h" or arg == "--help"):
            print("usage: xkcdpwgen [-h] [-w WORDS] [-c CAPS] [-n NUMBERS] [-s SYMBOLS]\n")
            print("Generate a secure, memorable password using the XKCD method\n")
            print("optional arguments:\n")
            print("\t-h, --help            show this help message and exit\n")
            print("\t-w WORDS, --words WORDS\n")
            print("\t\tinclude WORDS words in the password (default=4)\n")
            print("\t-c CAPS, --caps CAPS  capitalize the first letter of CAPS random words\n")
            print("\t\t(default=0)\n")
            print("\t-n NUMBERS, --numbers NUMBERS\n")
            print("\t\tinsert NUMBERS random numbers in the password\n")
            print("\t\t(default=0)\n")
            print("\t-s SYMBOLS, --symbols SYMBOLS\n")
            print("\t\tinsert SYMBOLS random symbols in the password\n")
            print("\t\t(default=0)\n")
            doGeneration = False
        if(arg == "-w" or arg == "--words"):
            numWords = int(sys.argv[i + 1])
        if(arg == "-c" or arg == "--caps"):
            numCaps = int(sys.argv[i + 1])
        if(arg == "-n" or arg == "--numbers"):
            numNumbers = int(sys.argv[i + 1])
        if(arg == "-s" or arg == "--symbols"):
            numSymbols = int(sys.argv[i + 1])
    if (doGeneration):
        print(generatePassword(numWords, numCaps, numNumbers, numSymbols))