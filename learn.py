import json, sys, os

def readArgs():
    numArgs = len(sys.argv) - 1
    dictFile = "dict.json"
    inputFile = ""

    if numArgs >= 1: dictFile = sys.argv[1]
    if numArgs >= 2: inputFile = sys.argv[2]

    return dictFile, inputFile

def loadDict(filename):
    if not os.path.exists(filename):
        with open(filename, "w") as File: json.dump({}, File)

    with open(filename, "r") as File: dictionary = json.load(File)
    return dictionary

def learn(dict, input):
    tokens = input.split(" ")
    for i in range(0, len(tokens)-1):
        currentWord = tokens[i]
        nextWord = tokens[i+1]

        if currentWord not in dict: dict[currentWord] = {nextWord : 1}
        else:
            allNextWords = dict[currentWord]
            if nextWord not in allNextWords: dict[currentWord][nextWord] = 1
            else: dict[currentWord][nextWord] += 1

    return dict

def updateFile(filename, dictionary):
    with open(filename, "w") as File: json.dump(dictionary, File)

def main():
    dictFile, inputFile = readArgs()
    dictionary = loadDict(dictFile)
    if inputFile == "":
        while True:
            userInput = input("> ")
            if userInput == "": break
            dictionary = learn(dictionary, userInput)
            updateFile(dictFile, dictionary)

    else: print("Not found")

main()
